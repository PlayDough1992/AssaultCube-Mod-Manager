# AssaultCube Mod Development Guide

## Requirements
- Python 3.11+
- AC Mod Manager (installed)
- AssaultCube 1.3.0.2

## ⚠️ Memory Address Disclaimer
The provided addresses and pointers are specific to AssaultCube 1.3.0.2 and may not work on:
- Different game versions
- Different machines/systems
- Different memory layouts
- After game updates

Always verify addresses before distributing mods.

## Memory Addresses
```
Base Address: 0x400000 (AC.exe)
Player Base: 0x17E0A8   # Points to 0x57E0A8

Common Pointers:
Health: [base + 0x17E0A8] + 0xEC
Ammo: [base + 0x17E0A8] + 0x150
```

## Creating a Mod
Create a new `.py` file in your development folder:

```python
from mods.mod_base import ACMod

class YourMod(ACMod):
    def __init__(self):
        super().__init__()
        self.name = "Your Mod Name"
        self.description = "Mod description"
        self.base_offset = 0x17E0A8  # Player base
        self.monitoring = False

    def on_enable(self):
        """Called when mod is enabled"""
        self.monitoring = True
        print(f"[{self.name}] Enabled")

    def on_disable(self):
        """Called when mod is disabled"""
        self.monitoring = False
        print(f"[{self.name}] Disabled")

    def update(self):
        """Called every tick while enabled"""
        if not self.monitoring:
            return
        # Your mod logic here
```

## Example Mod - Infinite Health

```python
from mods.mod_base import ACMod

class InfiniteHealth(ACMod):
    def __init__(self):
        super().__init__()
        self.name = "Infinite Health"
        self.description = "Maintains 100 health"
        
        # Memory addresses
        self.base_offset = 0x17E0A8  # Points to 0x57E0A8
        self.health_offset = 0xEC    # Health offset
        
        # Settings
        self.target_health = 100
        self.monitoring = False
        self.last_health = None

    def get_health(self):
        """Read health through validated pointer chain"""
        try:
            base_addr = self.pm.base_address + self.base_offset
            ptr = self.pm.read_int(base_addr)
            return self.pm.read_int(ptr + self.health_offset)
        except Exception as e:
            print(f"[{self.name}] Failed to read health: {e}")
            return None

    def set_health(self, value):
        """Set health to specified value"""
        try:
            base_addr = self.pm.base_address + self.base_offset
            ptr = self.pm.read_int(base_addr)
            self.pm.write_int(ptr + self.health_offset, value)
            return True
        except Exception as e:
            print(f"[{self.name}] Failed to write health: {e}")
            return False

    def update(self):
        if not self.monitoring:
            return
            
        try:
            current_health = self.get_health()
            if current_health is not None and current_health < self.target_health:
                if self.set_health(self.target_health):
                    print(f"[{self.name}] Health restored: {current_health} -> {self.target_health}")
        except Exception as e:
            if not hasattr(self, 'last_error') or str(e) != self.last_error:
                print(f"[{self.name}] Error: {e}")
                self.last_error = str(e)

    def on_enable(self):
        self.monitoring = True
        self.last_health = self.get_health() or self.target_health
        print(f"[{self.name}] Monitoring health at {hex(self.base_offset)} -> [ptr + {hex(self.health_offset)}]")
        print(f"[{self.name}] Enabled")

    def on_disable(self):
        self.monitoring = False
        print(f"[{self.name}] Disabled")
```

## Building Your Mod

1. Save your mod as `your_mod.py`
2. Run the mod compiler:
```powershell
python mod_compiler.py your_mod.py
```
3. Place the generated `.acm` file in the AC Mod Manager's `mods` folder

## Best Practices
- Always use try/except for memory operations
- Check `self.monitoring` state in update()
- Clean up resources in on_disable()
- Use descriptive names
- Add error handling
- Validate pointer chains
- Print helpful debug messages
- Handle null pointers

## Memory Operations
```python
# Read operations
value = self.pm.read_int(address)    # Read 32-bit integer
value = self.pm.read_float(address)  # Read float

# Write operations
self.pm.write_int(address, value)    # Write 32-bit integer
self.pm.write_float(address, value)  # Write float
```
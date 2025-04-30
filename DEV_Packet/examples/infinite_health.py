from mods.mod_base import ACMod
import time

class InfiniteHealth(ACMod):
    """Example mod that demonstrates health manipulation"""
    
    def __init__(self):
        super().__init__()
        self.name = "Infinite Health"
        self.description = "Maintains 100 health"
        
        # Memory addresses (from working Die Hard mod)
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
        """Keep health at target value"""
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
# AssaultCube Mod Manager - Developer Documentation
## Version 1.5.0

### Important Notice
Starting with ACMM v1.5.0, mods can only be created using the official natives documented below. This ensures compatibility and security across all mods. Additional natives will be introduced in future updates.

## Native Functions

### Python Natives

#### Player State
- `get_health() -> int`
  - Returns current player health value
  - Range: 0-100

- `set_health(value: int) -> bool`
  - Sets player health to specified value
  - Range: 0-100
  - Returns True if successful

- `get_ammo() -> int`
  - Returns current ammo count
  - Primary weapon ammo

- `set_ammo(value: int) -> bool`
  - Sets primary weapon ammo to specified value
  - Returns True if successful

- `reset_player() -> bool`
  - Resets player to default state
  - Health = 100
  - Ammo = 30
  - Returns True if successful

### Lua Natives

#### Player Functions
- `natives.safeGetHealth()`
  - Gets current health
  - Returns: number (0-100)

- `natives.safeSetHealth(value)`
  - Sets player health
  - Parameter: number (0-100)

- `natives.safeGetAmmo()`
  - Gets current primary weapon ammo
  - Returns: number

- `natives.safeSetAmmo(value)`
  - Sets primary weapon ammo
  - Parameter: number

- `natives.resetPlayer()`
  - Resets player to default state
  - Health = 100, Ammo = 30

## Example Usage

### Python Example
```python
def update(self):
    if self.enabled and self.natives:
        current_health = self.natives.get_health()
        current_ammo = self.natives.get_ammo()
        
        if current_health < 30:
            self.natives.set_health(100)
            self.natives.set_ammo(30)
```

### Lua Example
```lua
function update()
    if natives then
        local health = natives.safeGetHealth()
        local ammo = natives.safeGetAmmo()
        
        if health < 30 then
            natives.safeSetHealth(100)
            natives.safeSetAmmo(30)
        end
    end
end
```

## Mod Lifecycle Methods

### Python Mods
- `__init__(self)`
  - Constructor, set mod name and description
- `update(self)`
  - Called every game tick when mod is enabled

### Lua Mods
- `onEnable()`
  - Called when mod is enabled
  - Return true for successful initialization
- `update()`
  - Called every game tick while enabled
- `onDisable()`
  - Called when mod is disabled
  - Clean up resources

## Upcoming Features
Future ACMM updates will introduce new natives for:
- Secondary weapon ammo
- Armor management
- Team operations
- Map/world interaction
- Network state

## Security Notes
- All mods must use these natives exclusively
- Direct memory manipulation outside these natives is not supported
- Mods attempting to bypass these restrictions may be blocked

## Support
For questions, issues, or to share your mods, visit:
- GitHub Repository: [Link to repo]
- Discord Community: [Link to Discord]

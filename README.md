# AssaultCube Mod Development Guide (Lua)

## Overview
This guide covers Lua mod development for the AssaultCube Mod Manager (ACMM). All mods use a natives-based system for safe game interaction without direct memory manipulation.

## Getting Started

### Basic Mod Structure
Every Lua mod must follow this structure:

```lua
-- Mod metadata (REQUIRED)
modName = "Your Mod Name"
modDescription = "Description of what your mod does"

-- Lifecycle functions
function onEnable()
    -- Called when mod is activated
    -- Return true if initialization successful
    return true
end

function onDisable()
    -- Called when mod is deactivated
    -- Cleanup code goes here
end

function update(deltaTime)
    -- Called every frame while mod is active
    -- deltaTime = time since last frame in seconds
    -- Your mod logic goes here
end
```

## Natives Reference

All game interactions must be done through the `natives` table. These functions provide safe, validated access to game memory and features. **Based on actual mod_base implementation:**

### 📊 Health System

#### Core Health Functions
```lua
natives.getHealth()
-- Returns: number or nil
-- Description: Get current player health value
-- Example: local health = natives.getHealth()

natives.setHealth(value)
-- Parameters: value (number) - Health amount to set  
-- Returns: boolean - Success/failure
-- Description: Set player health to specified value
-- Example: natives.setHealth(100)
```

#### Safe Health Wrappers
```lua
natives.safeGetHealth()
-- Returns: number (never nil, returns 0 if unavailable)
-- Description: Safe version of getHealth, always returns a number
-- Example: local health = natives.safeGetHealth()

natives.safeSetHealth(value)
-- Parameters: value (number) - Health amount to set
-- Returns: boolean - Success/failure  
-- Description: Safe version of setHealth with type validation
-- Example: natives.safeSetHealth(200)
```

### 🛡️ Armor System

#### Core Armor Functions
```lua
natives.getArmor()
-- Returns: number or nil
-- Description: Get current player armor value
-- Example: local armor = natives.getArmor()

natives.setArmor(value)
-- Parameters: value (number) - Armor amount to set
-- Returns: boolean - Success/failure
-- Description: Set player armor to specified value
-- Example: natives.setArmor(100)
```

#### Safe Armor Wrappers
```lua
natives.safeGetArmor()
-- Returns: number (never nil, returns 0 if unavailable)
-- Description: Safe version of getArmor, always returns a number
-- Example: local armor = natives.safeGetArmor()

natives.safeSetArmor(value)
-- Parameters: value (number) - Armor amount to set
-- Returns: boolean - Success/failure
-- Description: Safe version of setArmor with type validation
-- Example: natives.safeSetArmor(150)
```

### 🔫 Ammunition System

#### Core Ammo Functions
```lua
natives.getAmmo()
-- Returns: number or nil
-- Description: Get current weapon ammunition count
-- Example: local ammo = natives.getAmmo()

natives.setAmmo(value)
-- Parameters: value (number) - Ammo amount to set
-- Returns: boolean - Success/failure
-- Description: Set current weapon ammo to specified value
-- Example: natives.setAmmo(100)

natives.patchAmmo(enable)
-- Parameters: enable (boolean) - True to enable infinite ammo patch
-- Returns: boolean - Success/failure
-- Description: Toggle infinite ammunition patch
-- Example: natives.patchAmmo(true)
```

#### Safe Ammo Wrappers
```lua
natives.safeGetAmmo()
-- Returns: number (never nil, returns 0 if unavailable)
-- Description: Safe version of getAmmo, always returns a number
-- Example: local ammo = natives.safeGetAmmo()

natives.safeSetAmmo(value)
-- Parameters: value (number) - Ammo amount to set
-- Returns: boolean - Success/failure
-- Description: Safe version of setAmmo with type validation
-- Example: natives.safeSetAmmo(999)
```

### 🎮 Player Management

```lua
natives.resetPlayer()
-- Returns: boolean - Success/failure
-- Description: Reset player to default state (health: 100, ammo: 30)
-- Example: if natives.resetPlayer() then print("Player reset!") end
```

### 💬 Chat System

#### Chat Input Monitoring
```lua
natives.readChatInput()
-- Returns: string or nil
-- Description: Read current text in chat input field
-- Example: local input = natives.readChatInput()

natives.safeReadChatInput()
-- Returns: string (never nil, returns "" if unavailable)
-- Description: Safe version of readChatInput
-- Example: local input = natives.safeReadChatInput()
```

#### Chat Message Detection
```lua
natives.chatMessageDetect()
-- Returns: string or nil
-- Description: Detect incoming chat messages
-- Example: local message = natives.chatMessageDetect()

natives.safeChatMessageDetect()
-- Returns: string (never nil, returns "" if unavailable)
-- Description: Safe version of chatMessageDetect
-- Example: local message = natives.safeChatMessageDetect()
```

### 📝 Logging & Debug

#### File Logging
```lua
natives.logToFile(message, logFile)
-- Parameters: message (string), logFile (string, optional)
-- Returns: boolean - Success/failure
-- Description: Write message to specified log file
-- Example: natives.logToFile("Debug message", "mylog.txt")

natives.safeLogToFile(message, logFile)
-- Parameters: message (string), logFile (string, optional)
-- Returns: boolean - Success/failure
-- Description: Safe version with temp file fallback and type validation
-- Example: natives.safeLogToFile("Mod started successfully")
```

#### PowerShell Monitor
```lua
natives.launchPowerShellMonitor(scriptPath)
-- Parameters: scriptPath (string, optional) - Path to monitor script
-- Returns: boolean - Success/failure
-- Description: Launch PowerShell monitoring window
-- Example: natives.launchPowerShellMonitor("deps/monitor/monitor.ps1")

natives.safeLaunchPowerShellMonitor(scriptPath)
-- Parameters: scriptPath (string, optional) - Path to monitor script
-- Returns: boolean - Success/failure
-- Description: Safe version with default path fallback
-- Example: natives.safeLaunchPowerShellMonitor()
```

## Example Mods

### Simple Health Monitor
```lua
modName = "Health Monitor"
modDescription = "Logs health changes"

local lastHealth = 0

function onEnable()
    natives.safeLogToFile("Health Monitor started")
    return true
end

function update(deltaTime)
    local currentHealth = natives.safeGetHealth()
    if currentHealth ~= lastHealth then
        natives.safeLogToFile("Health changed: " .. lastHealth .. " -> " .. currentHealth)
        lastHealth = currentHealth
    end
end
```

### Auto-Heal Mod
```lua
modName = "Auto Heal"
modDescription = "Automatically heals when health is low"

function onEnable()
    return true
end

function update(deltaTime)
    local health = natives.safeGetHealth()
    if health < 50 then
        natives.safeSetHealth(100)
    end
end
```

### Chat Command System
```lua
modName = "Simple Commands"
modDescription = "Basic chat command system"

local lastMessage = ""

function onEnable()
    return true
end

function update(deltaTime)
    local message = natives.safeChatMessageDetect()
    
    if message ~= lastMessage and message ~= "" then
        if message == "!heal" then
            natives.safeSetHealth(100)
            natives.safeLogToFile("Heal command executed")
        elseif message == "!armor" then
            natives.safeSetArmor(100)
            natives.safeLogToFile("Armor command executed")
        end
        lastMessage = message
    end
end
```

## Best Practices

### Error Handling
```lua
function update(deltaTime)
    -- Always check if natives are available
    if not natives then
        return
    end
    
    -- Use safe wrappers for reliability
    local health = natives.safeGetHealth()
    
    -- Validate data before use
    if health > 0 and health < 50 then
        natives.safeSetHealth(100)
    end
end
```

### Performance Tips
- Use `safe*` functions for critical operations
- Cache values when possible to avoid repeated native calls
- Use deltaTime for time-based operations
- Avoid heavy operations in update() function

### Debugging
```lua
function onEnable()
    -- Enable PowerShell monitor for debugging
    natives.safeLaunchPowerShellMonitor()
    
    -- Log initialization
    natives.safeLogToFile("=== MOD STARTED ===")
    
    return true
end

function update(deltaTime)
    -- Log important state changes
    local health = natives.safeGetHealth()
    if health < 25 then
        natives.safeLogToFile("LOW HEALTH WARNING: " .. health)
    end
end
```

## Troubleshooting

### Common Issues
1. **"natives.* is nil"** - Check mod base version, requires mod_base152.acm
2. **Functions not working** - Ensure AssaultCube is running and mod is enabled
3. **Intermittent failures** - Use safe wrapper functions instead of direct natives

### Mod Base Requirements
- **REQUIRED**: mod_base152.acm (latest version)
- **NOT COMPATIBLE** with older mod base versions
- All natives require the latest mod base to function

### Debug Checklist
1. Check modName and modDescription are set
2. Verify onEnable() returns true
3. Use natives.safeLogToFile() for debugging
4. Test with simple natives first (getHealth, setHealth)

---

**Happy modding!** 🎮⚡





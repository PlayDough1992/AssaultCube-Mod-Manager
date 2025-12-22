# Commands Mod - Installation Guide

## Overview
The Commands mod provides a chat-based command system for AssaultCube with real-time monitoring capabilities. Execute powerful commands directly through in-game chat using the `::` prefix.

## ⚠️ IMPORTANT COMPATIBILITY NOTICE
**This mod is NOT backwards compatible and requires the latest mod base version.**

- **REQUIRES:** `mod_base152.acm` (latest mod base update)
- **NOT COMPATIBLE** with older mod base versions
- **NOT COMPATIBLE** with standard AssaultCube installations without ACMM

Make sure you have the latest ACMM installation with `mod_base152.acm` before installing this mod!

## Available Commands
- `::setLife <amount>` - Set player health
- `::setMetal <amount>` - Set player armor (metal = armor)
- `::setARAmmo <amount>` - Set assault rifle ammunition
- `::godMode` - Toggle god mode (maintains health: 300, ammo: 100, armor: 300)
- `::help` - Show available commands or get help for specific commands

## Installation Steps

### Step 1: Install the Commands Mod
1. Copy `Commands.acm` to your **ACMM mods folder**
   ```
   [ACMM Root Directory]/mods/Commands.acm
   ```
   
   **Example path:**
   ```
   D:\AssaultCube-Mod-Manager\mods\Commands.acm
   ```

### Step 2: Create Monitor Directory Structure
1. Navigate to your **ACMM root directory**
2. Create the following folder structure:
   ```
   [ACMM Root Directory]/deps/monitor/
   ```
   
   **Example path:**
   ```
   D:\AssaultCube-Mod-Manager\deps\monitor\
   ```

### Step 3: Install PowerShell Monitor Script
1. Copy `monitor.ps1` to the monitor folder you just created:
   ```
   [ACMM Root Directory]/deps/monitor/monitor.ps1
   ```
   
   **Example path:**
   ```
   D:\AssaultCube-Mod-Manager\deps\monitor\monitor.ps1
   ```

## Final Directory Structure
Your ACMM installation should look like this:
```
ACMM Root Directory/
├── mods/
│   ├── Commands.acm          ← Commands mod file
│   └── [other mod files]
├── deps/
│   └── monitor/
│       └── monitor.ps1       ← PowerShell monitor script
└── [other ACMM files]
```

## Usage Instructions

### Basic Usage
1. **Load the mod** in ACMM
2. **Join an AssaultCube game**
3. **Type commands in chat** starting with `::`

### Example Commands
```
::setLife 200        → Set health to 200
::setMetal 100       → Set armor to 100
::setARAmmo 999      → Set assault rifle ammo to 999
::godMode            → Toggle invincibility mode
::help               → Show all available commands
::help setLife       → Get help for setLife command
```

### Monitor Window
- A **PowerShell window will automatically open** when the mod loads
- This shows **real-time command detection and execution**
- The monitor is **optional** - commands work without it
- **Press Ctrl+C** in the PowerShell window to stop monitoring

## Features

### Command System
- **Chat-based control** - Execute commands through in-game chat
- **Case-insensitive** - `::setlife`, `::SetLife`, `::SETLIFE` all work
- **Error handling** - Invalid commands show helpful error messages
- **Help system** - Built-in command documentation

### God Mode
- **Health**: Maintained at 300 (instant healing)
- **Armor**: Maintained at 300 (instant repair)  
- **Ammo**: Maintained at 100 (infinite ammo)
- **Toggle**: Use `::godMode` to turn on/off
- **Real-time**: Monitors and restores stats every frame

### PowerShell Monitoring
- **Auto-launch** - Automatically opens when mod starts
- **Real-time logging** - See commands as they execute
- **Color-coded output** - Easy to read status messages
- **Command feedback** - See results and error messages

## Troubleshooting

### Commands Not Working
1. **Check mod installation** - Ensure `Commands.acm` is in the mods folder
2. **Verify mod is loaded** - Check ACMM mod list
3. **Use correct prefix** - Commands must start with `::`
4. **Check spelling** - Use `::help` to see available commands

### Monitor Not Opening
1. **Check directory structure** - Ensure `deps/monitor/monitor.ps1` exists
2. **PowerShell permissions** - Make sure PowerShell can execute scripts
3. **Manual launch** - You can run `monitor.ps1` manually if needed

### Native Function Errors
- **"Health function not available"** - Check mod base version, MUST use mod_base152.acm
- **"Armor function not available"** - Ensure you have mod_base152.acm installed
- **"Ammo function not available"** - Verify mod_base152.acm compatibility

### Mod Base Compatibility
- **Check mod base version** - Must be `mod_base152.acm`
- **Update ACMM** - Get latest version with mod_base152.acm
- **Remove old mod bases** - Delete older versions to avoid conflicts

## Requirements
- **ACMM (AssaultCube Mod Manager)** - Latest version
- **mod_base152.acm** - REQUIRED (latest mod base version)
- **AssaultCube 1.3.0.2** - Compatible game version
- **PowerShell** - For monitoring (Windows built-in)

### ⚠️ Critical Requirements
- This mod **ONLY works with mod_base152.acm**
- **Will NOT work** with older mod base versions (mod_base151.acm, mod_base150.acm, etc.)
- **Will NOT work** with standard AssaultCube without ACMM

## Support
For issues or questions about the Commands mod:
1. Check that your ACMM installation is working properly
2. Verify all files are in the correct locations
3. Ensure you're using the latest mod base version
4. Test with simple commands like `::help` first

---

**Enjoy your enhanced AssaultCube experience with powerful chat commands!** 🎮⚡
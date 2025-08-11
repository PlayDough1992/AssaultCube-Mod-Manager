# 🎮 AssaultCube Mod Development Guide

*A comprehensive guide for developing AssaultCube mods using Lua*

---

## 📋 Table of Contents
- [🌍 Languages / Idiomas / Языки](#-languages--idiomas--языки)
- [⚡ Quick Start](#-quick-start)
- [📋 Requirements](#-requirements)
- [🔧 Available APIs](#-available-apis)
- [📖 Complete Example](#-complete-example)
- [📦 Installation & Distribution](#-installation--distribution)
- [🏗️ Development Workflow](#️-development-workflow)
- [⚖️ Legal Notice - Source Code Rights](#️-legal-notice---source-code-rights)
- [💡 Best Practices](#-best-practices)
- [📚 Common Patterns](#-common-patterns)

---

## 🌍 Languages / Idiomas / Языки

| Language | Link |
|----------|------|
| 🇺🇸 English | [Current Document](#-english-version) |
| 🇪🇸 Español | [Ver en Español](#-versión-en-español) |
| 🇷🇺 Русский | [Читать на русском](#-русская-версия) |

---

# 🇺🇸 English Version

## ⚡ Quick Start

**TL;DR**: Create `.lua` file → Write mod → **COMPILE** → Distribute

> ⚠️ **CRITICAL**: Only **compiled** mods work! Raw `.lua` files are ignored.

---

## 📋 Requirements

### 🔴 MANDATORY Compilation
```
❌ Raw .lua files → WILL NOT WORK
✅ Compiled mods → WILL WORK
```

**The mod manager will ONLY load compiled mods. No exceptions.**

### 📁 File Structure
- Single `.lua` source file
- File name = mod name (e.g., `regenerative_health.lua`)
- Must be compiled before distribution

### 🧩 Required Code Components
Every mod MUST include:

1. **Mod Information** (Global variables):
```lua
modName = "Your Mod Name"
modDescription = "What your mod does"
```

2. **Core Functions** (Global functions):
```lua
function onEnable()  -- Called when enabled
    return true      -- Return true for success
end

function onDisable() -- Called when disabled
end

function update()    -- Called every game tick
    -- Your mod logic here
end
```

---

## 🔧 Available APIs

### 👤 Player Functions
| Function | Description | Parameters/Returns |
|----------|-------------|-------------------|
| `natives.safeGetHealth()` | Get current health | Returns: number (0-100) |
| `natives.safeSetHealth(value)` | Set player health | Parameter: number (0-100) |
| `natives.safeGetAmmo()` | Get primary weapon ammo | Returns: number |
| `natives.safeSetAmmo(value)` | Set primary weapon ammo | Parameter: number |
| `natives.resetPlayer()` | Reset to default state | Health=100, Ammo=30 |

---

## 📖 Complete Example

**Regenerative Health Mod** - Heals player up to 50 health when below 50:

```lua
-- Mod Information
modName = "Regenerative Health"
modDescription = "Regenerates health up to 50 maximum at 5 health per second whenever below 50%"

-- Settings
local isRegenerating = false
local lastRegenerationTime = 0
local regenerationRate = 5
local maxHealthLimit = 50
local regenerationInterval = 1.0

-- Called when mod is enabled
function onEnable()
    isRegenerating = false
    lastRegenerationTime = os.clock()
    print("Regenerative Health Mod enabled!")
    return true
end

-- Called when mod is disabled
function onDisable()
    isRegenerating = false
    print("Regenerative Health Mod disabled!")
end

-- Called every tick while enabled
function update()
    local currentHealth = natives.safeGetHealth()
    if not currentHealth then return end
    processHealthRegeneration(currentHealth)
end

-- Regeneration logic
function processHealthRegeneration(currentHealth)
    local currentTime = os.clock()
    
    if currentHealth < maxHealthLimit and not isRegenerating then
        isRegenerating = true
        lastRegenerationTime = currentTime
        print("Health regeneration started at " .. currentHealth .. " health")
        
    elseif isRegenerating and currentHealth < maxHealthLimit then
        if currentTime - lastRegenerationTime >= regenerationInterval then
            local newHealth = math.min(currentHealth + regenerationRate, maxHealthLimit)
            natives.safeSetHealth(newHealth)
            lastRegenerationTime = currentTime
            print("Health regenerated: " .. currentHealth .. " -> " .. newHealth)
            
            if newHealth >= maxHealthLimit then
                isRegenerating = false
                print("Health regeneration completed")
            end
        end
        
    elseif isRegenerating and currentHealth >= maxHealthLimit then
        isRegenerating = false
        print("Health regeneration stopped")
    end
end
```

---

## 📦 Installation & Distribution

### 🔨 For Developers:
1. ✍️ Write your `.lua` mod
2. 🧪 Test your logic  
3. ⚙️ **COMPILE using mod compiler tool**
4. 📤 Distribute compiled mod

### 👥 For Users:
1. 📥 Download compiled mod
2. 📂 Place in AssaultCube Mod Manager Mods directory
   - Usually: `C:\Program Files (x86)\AssaultCube Mod Manager\mods`
3. ▶️ Load through mod manager
4. ✅ Enable to use

> ⚠️ **Important**: Only compiled mods appear in mod manager!

---

## 🏗️ Development Workflow

### 🎯 Creating Mods
```
Write Code → Test Logic → COMPILE → Distribute
```

### 📤 Sharing Open Source
- ✅ **OPTIONAL**: Share source code if you want
- ❌ **NOT REQUIRED**: No obligation to share
- 🔒 **YOUR CHOICE**: Keep private or share openly
- 👥 **USER RESPONSIBILITY**: Others must compile shared source

---

## ⚖️ Legal Notice - Source Code Rights

### 🚨 CRITICAL LEGAL INFORMATION

```
📜 NO REQUIREMENT to release source code
🆓 VOLUNTARY ONLY - your choice
✅ NO VIOLATION keeping source private
🏆 FULL OWNERSHIP of your code
❌ NO OBLIGATION to share anything
👑 CREATOR'S CHOICE always respected
```

**You control your source code completely. Sharing is optional, not required.**

---

## 💡 Best Practices

### ⏰ Timing
- Use `os.clock()` for timing
- Store timing variables as local
- Check intervals before expensive operations

### 🔒 State Management  
- Use local variables for state
- Reset state in `onEnable()`/`onDisable()`
- Always check if values exist

### ⚡ Performance
- Keep `update()` lightweight
- Use timing intervals for periodic tasks
- Avoid unnecessary calculations

---

## 📚 Common Patterns

### ⏱️ Timer-Based Operations
```lua
local lastActionTime = 0
local actionInterval = 1.0

function update()
    local currentTime = os.clock()
    if currentTime - lastActionTime >= actionInterval then
        -- Perform action
        lastActionTime = currentTime
    end
end
```

### 🔄 State Management
```lua
local isActive = false

function onEnable()
    isActive = true
    return true
end

function onDisable()
    isActive = false
end
```

### 🛡️ Safe API Usage
```lua
function update()
    local health = natives.safeGetHealth()
    if health then
        if health < 50 then
            natives.safeSetHealth(math.min(health + 5, 50))
        end
    end
end
```

---

# 🇪🇸 Versión en Español

## ⚡ Inicio Rápido

**Resumen**: Crear archivo `.lua` → Escribir mod → **COMPILAR** → Distribuir

> ⚠️ **CRÍTICO**: ¡Solo los mods **compilados** funcionan! Los archivos `.lua` sin compilar son ignorados.

---

## 📋 Requisitos

### 🔴 Compilación OBLIGATORIA
```
❌ Archivos .lua sin compilar → NO FUNCIONARÁN
✅ Mods compilados → FUNCIONARÁN
```

**El gestor de mods SOLO cargará mods compilados. Sin excepciones.**

### 📁 Estructura de Archivos
- Un solo archivo fuente `.lua`
- Nombre del archivo = nombre del mod (ej: `regenerative_health.lua`)
- Debe compilarse antes de la distribución

### 🧩 Componentes de Código Requeridos
Todo mod DEBE incluir:

1. **Información del Mod** (Variables globales):
```lua
modName = "Nombre de tu Mod"
modDescription = "Qué hace tu mod"
```

2. **Funciones Principales** (Funciones globales):
```lua
function onEnable()  -- Llamada al activar
    return true      -- Retorna true para éxito
end

function onDisable() -- Llamada al desactivar
end

function update()    -- Llamada cada tick del juego
    -- Tu lógica del mod aquí
end
```

---

## 🔧 APIs Disponibles

### 👤 Funciones del Jugador
| Función | Descripción | Parámetros/Retorna |
|---------|-------------|-------------------|
| `natives.safeGetHealth()` | Obtener salud actual | Retorna: número (0-100) |
| `natives.safeSetHealth(value)` | Establecer salud del jugador | Parámetro: número (0-100) |
| `natives.safeGetAmmo()` | Obtener munición del arma principal | Retorna: número |
| `natives.safeSetAmmo(value)` | Establecer munición del arma principal | Parámetro: número |
| `natives.resetPlayer()` | Resetear a estado por defecto | Salud=100, Munición=30 |

---

## ⚖️ Aviso Legal - Derechos del Código Fuente

### 🚨 INFORMACIÓN LEGAL CRÍTICA

```
📜 NO ES OBLIGATORIO liberar código fuente
🆓 SOLO VOLUNTARIO - tu elección
✅ NO ES VIOLACIÓN mantener el código privado
🏆 PROPIEDAD COMPLETA de tu código
❌ NO HAY OBLIGACIÓN de compartir nada
👑 ELECCIÓN DEL CREADOR siempre respetada
```

**Tú controlas tu código fuente completamente. Compartir es opcional, no obligatorio.**

---

# 🇷🇺 Русская версия

## ⚡ Быстрый старт

**Коротко**: Создать файл `.lua` → Написать мод → **СКОМПИЛИРОВАТЬ** → Распространить

> ⚠️ **КРИТИЧНО**: Работают только **скомпилированные** моды! Сырые файлы `.lua` игнорируются.

---

## 📋 Требования

### 🔴 ОБЯЗАТЕЛЬНАЯ компиляция
```
❌ Сырые .lua файлы → НЕ БУДУТ РАБОТАТЬ
✅ Скомпилированные моды → БУДУТ РАБОТАТЬ
```

**Менеджер модов загружает ТОЛЬКО скомпилированные моды. Без исключений.**

### 📁 Структура файлов
- Один исходный файл `.lua`
- Имя файла = имя мода (например: `regenerative_health.lua`)
- Должен быть скомпилирован перед распространением

### 🧩 Обязательные компоненты кода
Каждый мод ДОЛЖЕН включать:

1. **Информация о моде** (Глобальные переменные):
```lua
modName = "Название вашего мода"
modDescription = "Что делает ваш мод"
```

2. **Основные функции** (Глобальные функции):
```lua
function onEnable()  -- Вызывается при включении
    return true      -- Возвращает true при успехе
end

function onDisable() -- Вызывается при отключении
end

function update()    -- Вызывается каждый тик игры
    -- Логика вашего мода здесь
end
```

---

## 🔧 Доступные API

### 👤 Функции игрока
| Функция | Описание | Параметры/Возвращает |
|---------|----------|---------------------|
| `natives.safeGetHealth()` | Получить текущее здоровье | Возвращает: число (0-100) |
| `natives.safeSetHealth(value)` | Установить здоровье игрока | Параметр: число (0-100) |
| `natives.safeGetAmmo()` | Получить патроны основного оружия | Возвращает: число |
| `natives.safeSetAmmo(value)` | Установить патроны основного оружия | Параметр: число |
| `natives.resetPlayer()` | Сбросить к состоянию по умолчанию | Здоровье=100, Патроны=30 |

---

## ⚖️ Правовое уведомление - Права на исходный код

### 🚨 КРИТИЧЕСКАЯ ПРАВОВАЯ ИНФОРМАЦИЯ

```
📜 НЕ ТРЕБУЕТСЯ публиковать исходный код
🆓 ТОЛЬКО ДОБРОВОЛЬНО - ваш выбор
✅ НЕ НАРУШЕНИЕ держать код приватным
🏆 ПОЛНАЯ СОБСТВЕННОСТЬ на ваш код
❌ НЕТ ОБЯЗАТЕЛЬСТВ делиться чем-либо
👑 ВЫБОР СОЗДАТЕЛЯ всегда уважается
```

**Вы полностью контролируете свой исходный код. Делиться необязательно, это ваш выбор.**

---

## 📄 License

This guide and example code are provided as-is for educational and development purposes.

**Complete intellectual property protection for mod creators. Source code sharing is entirely optional and voluntary.**

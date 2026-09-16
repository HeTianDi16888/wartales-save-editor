# Windows 11 Setup Guide

## Quick Start (Easiest Way)

### Step 1: Download the Executable
1. Go to [Releases](https://github.com/HeTianDi16888/wartales-save-editor/releases)
2. Download `Wartales-Save-Editor.zip`
3. Extract it to any folder (e.g., `C:\Users\YourName\Downloads\Wartales-Save-Editor`)

### Step 2: Run the Program
1. Double-click `Wartales Save Editor.exe`
2. The GUI window will open
3. Click "Open Save File" and navigate to your saves

**That's it! No installation needed.**

---

## Build Your Own Executable (Advanced)

If you want to compile the executable yourself:

### Prerequisites
1. **Install Python 3.8+**
   - Download from [python.org](https://www.python.org/downloads/)
   - **Important:** Check "Add Python to PATH" during installation
   - Verify installation: Open Command Prompt and type `python --version`

2. **Install Git** (optional, for cloning)
   - Download from [git-scm.com](https://git-scm.com/)

### Build Steps

#### Option A: Using Command Prompt

1. **Open Command Prompt** (`Win + R`, type `cmd`, press Enter)

2. **Navigate to project folder:**
   ```cmd
   cd C:\Users\YourName\Downloads\wartales-save-editor
   ```

3. **Install dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```

4. **Build the executable:**
   ```cmd
   build.bat
   ```

5. **Find the executable:**
   - Look in the `dist` folder
   - File: `Wartales Save Editor.exe`
   - Copy it wherever you want

#### Option B: Using Git (if installed)

1. **Open Command Prompt**

2. **Clone the repository:**
   ```cmd
   git clone https://github.com/HeTianDi16888/wartales-save-editor.git
   cd wartales-save-editor
   ```

3. **Install and build:**
   ```cmd
   pip install -r requirements.txt
   build.bat
   ```

---

## Troubleshooting

### "Python is not recognized"
**Solution:**
- Reinstall Python and make sure to check "Add Python to PATH"
- Or manually add Python to PATH:
  1. Press `Win + X` and open "System"
  2. Click "Advanced system settings"
  3. Click "Environment Variables"
  4. Under "User variables", click "New"
  5. Variable name: `PATH`
  6. Variable value: `C:\Users\YourName\AppData\Local\Programs\Python\Python311` (adjust version)
  7. Click OK

### "pip: command not found"
**Solution:**
- Make sure Python was installed with pip
- Try: `python -m pip install -r requirements.txt`

### "PyInstaller not found"
**Solution:**
- Run: `pip install pyinstaller`

### Antivirus blocks the executable
**Solution:**
- This is normal for custom-built executables
- Add the file to your antivirus whitelist
- Or download from Releases page (pre-built version)

### Application won't open
**Solution:**
- Run as Administrator: Right-click → "Run as administrator"
- Check that you have read/write permissions to save files
- Try rebuilding the executable

---

## Finding Your Save Files

**Default location:**
```
C:\Users\<YourUsername>\AppData\LocalLow\Shiro Games\Wartales\savegames
```

**Quick access:**
1. Press `Win + R`
2. Copy-paste this: `%APPDATA%\..\LocalLow\Shiro Games\Wartales\savegames`
3. Press Enter

**Backup your saves first!**

---

## Running from Source (No Executable Needed)

If you prefer not to build an executable, you can run directly from Python:

1. Install Python 3.8+
2. Open Command Prompt
3. Navigate to the project folder
4. Run: `python main.py`

The GUI will open directly.

---

## System Requirements

- **OS:** Windows 7, 10, or 11
- **RAM:** 512 MB minimum (1 GB recommended)
- **Disk Space:** 100 MB free
- **Python:** 3.8+ (only if running from source)
- **.NET Framework:** Windows typically includes this

---

## Uninstallation

Simply delete the folder and executable. No registry entries or system changes.

---

## Need Help?

- Check the [README.md](README.md) for feature documentation
- Report issues on [GitHub Issues](https://github.com/HeTianDi16888/wartales-save-editor/issues)
- Always keep backups of your save files!

---

**Happy editing! 🎮**

# Publishing Guide for Wartales Save Editor

## How to Create a Release and Publish the Executable

### Step 1: Build the Executable on Your Computer

1. **Open Command Prompt** (`Win + R`, type `cmd`)

2. **Navigate to the project folder:**
   ```bash
   cd path\to\wartales-save-editor
   ```

3. **Install PyInstaller** (if not already installed):
   ```bash
   pip install pyinstaller
   ```

4. **Build the executable:**
   ```bash
   build.bat
   ```

5. **Verify the build:**
   - Open the `dist` folder
   - You should see `Wartales Save Editor.exe`

### Step 2: Create a GitHub Release

1. **Go to your repository:**
   - https://github.com/HeTianDi16888/wartales-save-editor

2. **Click "Releases"** on the right side

3. **Click "Create a new release"**

4. **Fill in the release details:**
   - **Tag version:** `v1.0.0` (or your version number)
   - **Release title:** `Wartales Save Editor v1.0.0`
   - **Description:** Use the template below

5. **Upload the executable:**
   - Click "Attach binaries by dropping them here or selecting them"
   - Select `dist/Wartales Save Editor.exe`

6. **Publish the release:**
   - Click "Publish release"

### Release Description Template

```markdown
# Wartales Save Editor v1.0.0

A user-friendly GUI application for editing Wartales character stats, traits, equipment, and inventory.

## ✨ Features
- **Edit Character Stats** - Strength, dexterity, constitution, wisdom, intelligence, speed
- **Manage Traits & Perks** - View and modify character traits directly
- **Equipment Management** - Edit weapons, armor, helmets, boots, and accessories
- **Inventory System** - Add, remove, or modify inventory items
- **Party Support** - Edit all characters and companions
- **Safety First** - Automatic backup creation with timestamps

## 🚀 Quick Start
1. Download `Wartales Save Editor.exe`
2. Run it directly (no installation needed!)
3. Click "Open Save File"
4. Navigate to: `C:\Users\YourName\AppData\LocalLow\Shiro Games\Wartales\savegames`
5. Select your save file and start editing!

## 💻 System Requirements
- **OS:** Windows 7, 10, or 11
- **RAM:** 512 MB minimum
- **Disk Space:** 100 MB

## 📖 Documentation
- [README.md](https://github.com/HeTianDi16888/wartales-save-editor/blob/main/README.md) - Full documentation
- [SETUP_GUIDE.md](https://github.com/HeTianDi16888/wartales-save-editor/blob/main/SETUP_GUIDE.md) - Installation guide
- [Main repository](https://github.com/HeTianDi16888/wartales-save-editor) - Source code

## ⚠️ Important
- **Always backup your saves** before editing
- Modifying saves may corrupt your progress
- Use at your own risk
- Close Wartales before editing saves

## 🎮 Happy Modding!
Enjoy editing your Wartales adventure!
```

### Step 3: Verify the Release

1. Go to the Releases page
2. Download the executable from your new release
3. Test it on Windows 11
4. Verify it works correctly

### Step 4: Share Your Release

You can now share this link with others:
```
https://github.com/HeTianDi16888/wartales-save-editor/releases/latest
```

---

## Automated Releases (Optional)

If you want GitHub to automatically build releases when you create a tag:

1. Go to `.github/workflows/` folder in your repository
2. Create `build-release.yml` with the workflow content
3. Future tags will automatically build and release the executable

For now, manual building and uploading is the simplest approach.

---

## Troubleshooting

### "Build failed" or ".exe not created
- Make sure Python 3.8+ is installed
- Verify PyInstaller installed: `pip install pyinstaller`
- Check for syntax errors in `main.py`
- Try deleting `build/` and `dist/` folders and rebuilding

### Release won't upload
- Check file size (should be ~50-100 MB)
- Make sure you're logged into GitHub
- Try uploading again - sometimes GitHub needs a retry

### Executable runs but crashes
- Try running as Administrator
- Update to latest Python version
- Rebuild the executable

---

## What to Do After Publishing

✅ Test the released executable on a clean Windows 11 system
✅ Share the release link with friends
✅ Gather feedback from users
✅ Fix bugs and release updates as `v1.0.1`, `v1.1.0`, etc.

---

**Your Wartales Save Editor is ready for release! 🎉**

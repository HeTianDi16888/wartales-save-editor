# Wartales Save Editor

A user-friendly GUI application for editing Wartales character stats, traits, equipment, and inventory.

## Features

✨ **Complete Character Editing**
- Edit all character stats (strength, dexterity, constitution, wisdom, intelligence, speed)
- Modify basic attributes (level, health, experience)
- Edit additional stats (armor, dodge, crit chance, initiative)

✨ **Traits & Perks Management**
- View and edit character traits directly
- Support for status effects and perks

✨ **Equipment Management**
- Edit equipped items
- Slots: weapon, armor, helmet, boots, accessory

✨ **Inventory Management**
- Add, remove, or modify inventory items
- Direct JSON editing for advanced control

✨ **Character & Companion Support**
- Edit all party members
- Switch between characters easily

✨ **Safety Features**
- Automatic backup creation with timestamps
- JSON validation before saving
- File integrity checks

## Installation

### Option 1: Use Pre-built Executable (Easiest)

1. Download the latest release from the [Releases](https://github.com/HeTianDi16888/wartales-save-editor/releases) page
2. Extract the `.zip` file
3. Run `Wartales Save Editor.exe`
4. No installation needed!

### Option 2: Build from Source

**Prerequisites:**
- Windows 11
- Python 3.8 or higher

**Steps:**

1. Clone the repository:
```bash
git clone https://github.com/HeTianDi16888/wartales-save-editor.git
cd wartales-save-editor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

**Or build an executable:**

```bash
# Option A: Use the batch script (Windows)
build.bat

# Option B: Use PyInstaller directly
pyinstaller --onefile --windowed --name="Wartales Save Editor" main.py
```

The executable will be created in the `dist` folder.

## Usage

### Basic Workflow

1. **Open Save File**
   - Click "Open Save File"
   - Navigate to your Wartales save location (usually `C:\Users\YourUsername\AppData\LocalLow\Shiro Games\Wartales\savegames`)
   - Select a `.json` save file

2. **Select Character**
   - A list of characters/companions will appear on the left
   - Click any character to view/edit their stats

3. **Edit Stats**
   - Click the **Stats** tab
   - Modify any stat value in the text fields
   - Changes are reflected in real-time

4. **Edit Traits**
   - Click the **Traits** tab
   - Edit the JSON directly
   - Example: Add perks, status effects, or traits

5. **Edit Equipment**
   - Click the **Equipment** tab
   - Modify weapon, armor, and accessories
   - Edit JSON format directly

6. **Edit Inventory**
   - Click the **Inventory** tab
   - Add or remove items
   - Modify quantities

7. **Save Changes**
   - Click "Save Changes" to write modifications to your save file
   - A confirmation message will appear

8. **Create Backup**
   - Click "Create Backup" before making major changes
   - Backups are saved with timestamps

## Save File Location

**Default path:**
```
C:\Users\<YourUsername>\AppData\LocalLow\Shiro Games\Wartales\savegames
```

**To find your save files:**
1. Press `Win + R`
2. Type: `%APPDATA%\..\LocalLow\Shiro Games\Wartales\savegames`
3. Press Enter

## Common Stats

| Stat | Effect |
|------|--------|
| **Level** | Character level |
| **Health** | Current HP |
| **MaxHealth** | Maximum HP |
| **Experience** | XP towards next level |
| **Strength** | Melee damage, carrying capacity |
| **Constitution** | Max health, disease resistance |
| **Dexterity** | Dodge chance, critical hit chance |
| **Speed** | Turn order in combat |
| **Intelligence** | Spell power, crafting success |
| **Wisdom** | Healing power, status resistance |

## Tips & Best Practices

✅ **Always create a backup before major edits** - Click "Create Backup" first
✅ **Start with small changes** - Edit one stat at a time to find issues quickly
✅ **Don't exceed game limits** - Extremely high stats may cause game bugs
✅ **Keep health ≤ maxHealth** - Prevents potential issues
✅ **Use valid JSON in Traits/Equipment/Inventory tabs** - Syntax errors will prevent saving
✅ **Test your changes** - Load the save in-game to verify everything works

## Troubleshooting

### "Save file not found"
- Verify the file path is correct
- Check that Wartales is installed
- Ensure you have permission to access the file

### "Invalid JSON file"
- The save file might be corrupted
- Try using a backup save
- Close Wartales before editing saves

### "JSON error when saving"
- Check the Traits/Equipment/Inventory tabs for syntax errors
- Look for missing quotes or brackets
- Use a JSON validator if unsure

### Application crashes
- Try running as Administrator
- Update Python to the latest version
- Delete the `dist` folder and rebuild

## Advanced: Edit JSON Directly

If you're comfortable with JSON, you can:
1. Right-click the save file → Open with → Notepad
2. Use Ctrl+F to find specific characters
3. Edit the JSON directly
4. Save the file

Common structures:
```json
{
  "characters": [
    {
      "name": "Character Name",
      "level": 10,
      "stats": {
        "strength": 12,
        "dexterity": 10
      }
    }
  ]
}
```

## System Requirements

- **OS:** Windows 11 (also works on Windows 10, Windows 7)
- **RAM:** 512 MB minimum
- **Disk Space:** 50 MB
- **Python:** 3.8+ (only needed if running from source)

## Limitations

- Cannot edit game world/map data
- Cannot add new characters (only edit existing ones)
- Cannot modify story/quest progress
- Some game systems may not be exposed in the save file

## Safety & Legal

⚠️ **Use at your own risk:**
- Modifying saves may corrupt your progress
- Always keep backups
- The developer is not responsible for lost or corrupted saves
- This tool is for personal use only

**Regards to Shiro Games:** This tool is created for educational purposes and personal use. Respect the developers' rights to their work.

## Contributing

Found a bug? Have a feature request? Issues and pull requests are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Support

Need help? Check these resources:
- [Issues](https://github.com/HeTianDi16888/wartales-save-editor/issues) - Report bugs or request features
- [Discussions](https://github.com/HeTianDi16888/wartales-save-editor/discussions) - Ask questions
- Wartales Community - Share your experience with the editor

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Changelog

### v1.0.0 (Initial Release)
- ✨ Full character stat editing
- ✨ Traits and perks management
- ✨ Equipment editing
- ✨ Inventory management
- ✨ Automatic backup system
- ✨ Support for all party members

---

**Made with ❤️ for Wartales players**

Happy modding! 🎮

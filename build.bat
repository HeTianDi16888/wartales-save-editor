@echo off
echo Building Wartales Save Editor...
pyinstaller --onefile --windowed --icon=icon.ico --name="Wartales Save Editor" main.py
echo.
echo Build complete! The executable is in the 'dist' folder.
pause

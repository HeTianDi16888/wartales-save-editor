#!/bin/bash
# Build script for Wartales Save Editor
# This script builds the executable and prepares it for release

echo "Building Wartales Save Editor..."
echo "================================"

# Install dependencies
echo "Installing dependencies..."
pip install pyinstaller

# Build the executable
echo "Building executable..."
pyinstaller --onefile --windowed --name="Wartales Save Editor" main.py

# Check if build was successful
if [ -d "dist" ]; then
    echo ""
    echo "✓ Build successful!"
    echo "✓ Executable location: dist/Wartales Save Editor.exe"
    echo ""
    echo "Next steps:"
    echo "1. Create a release on GitHub"
    echo "2. Upload dist/Wartales Save Editor.exe to the release"
    echo "3. Upload README.md and SETUP_GUIDE.md"
else
    echo "✗ Build failed"
    exit 1
fi

@echo off
echo CK3 Terrain Mask Converter
echo ==========================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if Pillow is installed
python -c "import PIL" >nul 2>&1
if errorlevel 1 (
    echo Installing Pillow library...
    pip install Pillow
    if errorlevel 1 (
        echo Error: Failed to install Pillow
        pause
        exit /b 1
    )
)

REM Get input and output directories from user
set /p input_dir="Enter input directory (drag folder here): "
set /p output_dir="Enter output directory (drag folder here): "

REM Remove quotes if present
set input_dir=%input_dir:"=%
set output_dir=%output_dir:"=%

REM Ask for resolution choice
echo.
echo Choose conversion type:
echo 1. TC Sandbox scale (4608x2304) - Recommended
echo 2. Your heightmap size (4096x2048)
echo 3. Custom size
set /p choice="Enter choice (1-3): "

if "%choice%"=="1" (
    python "%~dp0ck3_mask_converter_console.py" "%input_dir%" "%output_dir%"
) else if "%choice%"=="2" (
    python "%~dp0ck3_mask_converter_console.py" "%input_dir%" "%output_dir%" 4096 2048
) else if "%choice%"=="3" (
    set /p custom_width="Enter width: "
    set /p custom_height="Enter height: "
    python "%~dp0ck3_mask_converter_console.py" "%input_dir%" "%output_dir%" !custom_width! !custom_height!
) else (
    echo Invalid choice
)

echo.
echo Done! Check the output directory for converted files.
pause

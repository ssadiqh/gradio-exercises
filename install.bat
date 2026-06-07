@echo off
REM Simple installation script for Gradio Exercises
REM No manual venv activation needed - this handles everything!

echo.
echo ============================================================
echo Gradio Exercises - Installation
echo ============================================================
echo.

REM Go to script directory
cd /d "%~dp0"

echo [*] Creating virtual environment...
python -m venv .venv

if errorlevel 1 (
    echo [ERROR] Failed to create virtual environment
    pause
    exit /b 1
)

echo [OK] Virtual environment created
echo.

echo [*] Installing dependencies (this may take 2-3 minutes)...
call .venv\Scripts\pip.exe install -q -r requirements.txt

if errorlevel 1 (
    echo [WARNING] Installation completed with warnings
) else (
    echo [OK] Dependencies installed successfully
)

echo.
echo [*] Verifying installation...
call .venv\Scripts\python.exe -c "import gradio; print('[OK] Gradio is ready!')"

if errorlevel 1 (
    echo [ERROR] Installation verification failed
    echo [TIP] Try running: .venv\Scripts\pip install -r requirements.txt
    pause
    exit /b 1
)

echo.
echo ============================================================
echo Installation Complete!
echo ============================================================
echo.
echo You can now run exercises:
echo   run_exercise.bat 1    - Exercise 1: Gradio Intro
echo   run_exercise.bat 2    - Exercise 2: Inputs/Outputs
echo   run_exercise.bat 3    - Exercise 3: Simple Chatbot
echo   run_exercise.bat 4    - Exercise 4: Advanced Chatbot
echo   run_exercise.bat 5    - Exercise 5: Multi-Turn Chat
echo.
pause
@echo off
REM Gradio Exercises - Quick Runner
REM Usage: run_exercise.bat [1-5] [variant]
REM Example: run_exercise.bat 1
REM Example: run_exercise.bat 2 analyzer

setlocal enabledelayedexpansion

if "%1"=="" (
    echo Usage: run_exercise.bat [1-5] [variant]
    echo.
    echo Examples:
    echo   run_exercise.bat 1           - Run Exercise 1 (default: sum calculator)
    echo   run_exercise.bat 1 joiner    - Run Exercise 1 (sentence joiner variant)
    echo   run_exercise.bat 2           - Run Exercise 2 (default: story builder)
    echo   run_exercise.bat 2 analyzer  - Run Exercise 2 (text analyzer variant)
    echo   run_exercise.bat 3           - Run Exercise 3 (simple chatbot)
    echo   run_exercise.bat 4           - Run Exercise 4 (advanced chatbot)
    echo   run_exercise.bat 5           - Run Exercise 5 (multi-turn chat)
    echo   run_exercise.bat 5 custom    - Run Exercise 5 (custom interface)
    echo.
    goto end
)

echo.
echo ============================================================
echo Gradio Exercises - Exercise %1 Runner
echo ============================================================
echo.

REM Activate virtual environment
echo [*] Activating virtual environment...
call .venv\Scripts\activate.bat

if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment
    echo [TIP] Create it first: python -m venv .venv
    goto end
)

echo [OK] Virtual environment activated
echo.

REM Run the exercise
if "%1"=="1" (
    echo [*] Running Exercise 1: Gradio Intro
    if "%2"=="joiner" (
        python 1_gradio_intro.py joiner
    ) else (
        python 1_gradio_intro.py
    )
) else if "%1"=="2" (
    echo [*] Running Exercise 2: Gradio Inputs/Outputs
    if "%2"=="analyzer" (
        python 2_gradio_inputs_outputs.py analyzer
    ) else (
        python 2_gradio_inputs_outputs.py
    )
) else if "%1"=="3" (
    echo [*] Running Exercise 3: Simple Chatbot
    python 3_simple_chatbot.py
) else if "%1"=="4" (
    echo [*] Running Exercise 4: Advanced Chatbot
    python 4_advanced_chatbot.py
) else if "%1"=="5" (
    echo [*] Running Exercise 5: Multi-Turn Chat
    if "%2"=="custom" (
        python 5_multi_turn_chat.py custom
    ) else (
        python 5_multi_turn_chat.py
    )
) else (
    echo [ERROR] Invalid exercise number: %1
    echo [TIP] Use 1-5
)

echo.
echo [*] Shutting down...
deactivate

:end
echo.
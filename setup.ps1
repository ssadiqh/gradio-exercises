# Gradio Exercises Setup Script for PowerShell
# Run this script to set up the environment

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Gradio Exercises - Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# Navigate to script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host ""
Write-Host "[*] Current directory: $PWD"
Write-Host "[*] Python version: $(python --version)"

# Check if venv exists
$venvPath = Join-Path $PWD ".venv"
if (Test-Path $venvPath) {
    Write-Host "[OK] Virtual environment exists"
} else {
    Write-Host "[*] Creating virtual environment..."
    python -m venv .venv
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[OK] Virtual environment created"
    } else {
        Write-Host "[ERROR] Failed to create virtual environment"
        exit 1
    }
}

# Activate venv
Write-Host ""
Write-Host "[*] Activating virtual environment..."
& .\.venv\Scripts\Activate.ps1

# Install requirements
Write-Host "[*] Installing dependencies..."
pip install -q -r requirements.txt
if ($LASTEXITCODE -eq 0) {
    Write-Host "[OK] Dependencies installed"
} else {
    Write-Host "[WARNING] Some dependencies may not have installed correctly"
}

# Verify
Write-Host "[*] Verifying installation..."
python -c "import gradio; print('[OK] Gradio ready')" 2>&1

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Now you can run exercises:" -ForegroundColor Yellow
Write-Host "  python 1_gradio_intro.py" -ForegroundColor White
Write-Host "  python 2_gradio_inputs_outputs.py" -ForegroundColor White
Write-Host "  python 3_simple_chatbot.py" -ForegroundColor White
Write-Host "  python 4_advanced_chatbot.py" -ForegroundColor White
Write-Host "  python 5_multi_turn_chat.py" -ForegroundColor White
Write-Host ""
Write-Host "Or use the batch script:" -ForegroundColor Yellow
Write-Host "  run_exercise.bat 4" -ForegroundColor White
Write-Host ""
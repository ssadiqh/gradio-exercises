#!/usr/bin/env python
"""
Setup script for Gradio Exercises
Installs virtual environment and dependencies
"""

import os
import sys
import subprocess

def run_command(cmd, description):
    """Run a command and report status"""
    print(f"\n[*] {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[OK] {description} complete")
            return True
        else:
            print(f"[ERROR] {description} failed")
            if result.stderr:
                print(f"    {result.stderr[:100]}")
            return False
    except Exception as e:
        print(f"[ERROR] {description}: {str(e)[:100]}")
        return False

def main():
    """Main setup function"""
    print("=" * 60)
    print("Gradio Exercises - Setup")
    print("=" * 60)

    # Check Python version
    print(f"\n[*] Python version: {sys.version.split()[0]}")

    # Create venv
    venv_path = os.path.join(os.getcwd(), ".venv")

    if os.path.exists(venv_path):
        print(f"\n[*] Virtual environment already exists at {venv_path}")
    else:
        if not run_command(f"{sys.executable} -m venv .venv", "Create virtual environment"):
            print("\n[ERROR] Failed to create virtual environment")
            return False

    # Determine pip path
    if sys.platform == "win32":
        pip_path = os.path.join(venv_path, "Scripts", "pip.exe")
    else:
        pip_path = os.path.join(venv_path, "bin", "pip")

    # Install requirements
    if not os.path.exists(pip_path):
        print(f"\n[ERROR] pip not found at {pip_path}")
        return False

    if not run_command(f"{pip_path} install -q -r requirements.txt", "Install dependencies"):
        print("[WARNING] Some dependencies may not have installed correctly")

    # Verify installation
    if sys.platform == "win32":
        python_path = os.path.join(venv_path, "Scripts", "python.exe")
    else:
        python_path = os.path.join(venv_path, "bin", "python")

    print(f"\n[*] Verifying installation...")
    result = subprocess.run(f"{python_path} -c \"import gradio; print('OK')\"",
                          shell=True, capture_output=True, text=True)

    if result.returncode == 0 and "OK" in result.stdout:
        print("[OK] Gradio successfully installed")
    else:
        print("[ERROR] Gradio installation verification failed")
        return False

    print("\n" + "=" * 60)
    print("Setup Complete!")
    print("=" * 60)

    print("\nNow you can run exercises using:")
    if sys.platform == "win32":
        print("  Option 1: .\\run_exercise.bat 1    (recommended)")
        print("  Option 2: .venv\\Scripts\\activate")
        print("            python 1_gradio_intro.py")
    else:
        print("  Option 1: bash run_exercise.sh 1")
        print("  Option 2: source .venv/bin/activate")
        print("            python 1_gradio_intro.py")

    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
import subprocess
import sys
import os

def build_executable(script_name):
    # Check if PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("PyInstaller not found. Installing it now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

    # Run PyInstaller command
    subprocess.run([sys.executable, "-m", "PyInstaller", "--onefile", script_name])

if __name__ == "__main__":
    script_name = "main.py"  # Change to your script's name if needed
    if not os.path.exists(script_name):
        print(f"{script_name} not found!")
    else:
        build_executable(script_name)
``

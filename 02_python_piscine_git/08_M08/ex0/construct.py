import sys
import os
import site

def main():
    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current python: {sys.executable}")
        print(f"Virtual environement: None detected")
        print()
        print("WARNING: You're in the global environement!\n" \
        "The machine can see everything you install")
        print(
            "To enter the construct, run:\n"
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scripts\\activate # On Windows\n"
            )
        print()
        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current python: {sys.executable}")
        print(f"Virtual Environement: {sys.prefix}")
        print(
            "SUCCESS: You're in an isolated environment! "
            "Safe to install packages without affecting "
            "the global system."
            )
        print(f"Package installation path: {site.getsitepackages()[0]}")

main()
        

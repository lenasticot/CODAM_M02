import pandas as pd

def check_pandas():
    try:
        print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
    except ModuleNotFoundError:
        "Pandas has not been correctly imported"

def main():
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")


main()
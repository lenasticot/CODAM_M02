import sys

def main():
    REQUIRED = ["numpy", "pandas", "matplotlib"]
    missing = []
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")
    for packs in REQUIRED:
        try: 
            __import__(packs)
        except ImportError:
            missing.append(packs)

    if missing:
        print(f"Missing dependency: {', '.join(missing)}")
        print("Run: pip install -r requirements.txt")
        print("Or: poetry install\n poetry run python loading.py")
        sys.exit(1)

    import numpy as np
    import pandas as pd
    import matplotlib
    import matplotlib.pyplot as plt
    import requests as rq
    print(f"[OK] panda({pd.__version__}) - Data manipulation ready")
    print(f"[OK] numpy({np.__version__}) - Data manipulation ready")
    print(f"[OK] requests({rq.__version__}) - Data manipulation ready")
    print(f"[OK] matplotlib({matplotlib.__version__}) - Data manipulation ready")
    print()
    np.random.seed(42)  # makes results reproducible, same numbers every run
    matrix = np.random.randint(0, 100, size=(10, 3))
    df = pd.DataFrame(matrix, columns=["red_pill", "blue_pill", "agents"])
    print(df)
    print(df.describe())
    df.plot(kind="bar", title="Matrix Data Analysis")
    plt.tight_layout()
    plt.savefig("matrix_plot.png")  # saves to a file
    print("Plot saved to matrix_plot.png")

main()
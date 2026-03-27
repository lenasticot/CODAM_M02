import sys


def command_analysis():
    print("=== Command quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
        i = 2
        for args in sys.argv[1:]:
            print(f"Argument {i - 1}: {args}")
            i += 1
    print(f"Total arguments: {len(sys.argv)}")


command_analysis()

def garden_operations(ope: str) -> str:
    if ope == "value":
        return int("merde")
    elif ope == "zero":
        return 5 / 0
    elif ope == "file":
        with open("missing.txt", "r") as file:
            content = file.read()
            return content
    elif ope == "key":
        plants = {"rose": 5, "tulip": 2, "hibiscus": 8}
        return plants["merde"]


def test_error_types():
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        result = garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    else:
        print(f"yes, {result} is a number\n")

    print("Testing ZeroDivisionError...")
    try:
        result = garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    else:
        print(f"The answer is: {result}\n")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as f:
        print(f"Caught FileNotFoundError: No such file {f.filename}'\n")
    else:
        print("The document is open\n")

    print("Testing KeyError...")
    try:
        key = garden_operations("key")
    except KeyError as k:
        print(f"Caught KeyError: {k} missing\n")
    else:
        print(f"{key} is well present\n")

    print("Testing multiple errors together...")
    operations = ["value", "zero", "file"]
    for ope in operations:
        try:
            garden_operations(ope)
        except (ValueError, ZeroDivisionError, FileNotFoundError):
            print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

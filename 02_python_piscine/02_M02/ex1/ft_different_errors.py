"""need to do a final check for the last sentence to be added"""
#need to double check the file_not_found error
def garden_operations():
    def value_error():
        return int("abc")
    def zero_division():
        return 5 / 0
    def file_not_found():
        open("missing.txt")
    def key_error():
        plants = {"rose": 5, "tulip": 2, "hibiscus": 8}
        return plants["apple"]
    return {
		"value": value_error,
		"zero": zero_division,
		"file": file_not_found,
		"key": key_error
	}
        
    

def test_error_types():
    """show each types of error happening
    catches each error and explains what went wrong
    demonstrates that your program continues running after each error
    shows how to catch multiple error types with one expect block"""

    print("=== Garden Error Types Demo ===")
    
    operations = garden_operations()
    print("Testing ValueError...")
    try:
        operations["value"]()
    except ValueError:
        print("Caught ValueError: invalid litteral for int()") 
    
    print("Testing ZeroDivisionError...")
    try:
        operations["zero"]()
    except ZeroDivisionError:
        print("Caugt ZeroDivisionError: division by zero")
    
    print("Testing FileNotFoundError...")
    try:
       operations["file"]()
    except FileNotFoundError as file:
        print(f"Caught FileNotFoundError: No such file {file}")
    
    print("Testing KeyError...")
    try:
        operations["key"]()
    except KeyError as key:
        print(f"Caugt KeyError: {key} missing")
    
    #try everything
    print("Testing multiple errors together...")
    try:
        operations["value"]()
    except Exception:
        print("Caught an error, but program continues!")
    
        print("All error types tested successfully!")

   
    

if __name__ == "__main__":
    
    test_error_types()
def raise_error():
    try:
        pass
    except:
        print("Caught PlantError:")
        
    try:
        pass
    except:
        print("Caught WaterError")
    
    try:
        pass
    except:
        print("Caught a garden error:")
    
    All custom error types work correctly

def print_error():
    pass

def show_error():
    pass

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
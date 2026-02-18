# your data validation layer must filter out bad data before
# it corrups your agricultural analytics

def check_temparture(temp_str):
    print(f"Testing temperature: {temp_str}")
    try:
        test = (int)(temp_str)
    except:
        print(f"Error: '{temp_str}' is not a valid number")
    else:
        if test > 0 and test < 40:
            print(f"Temperature {test}°C is perfect for plants!")
        elif test < 0:
            print(f"Error: {test}°C is too cold for plants (min 0°C)")
        elif test > 40:
            print(f"Error: {test}°C is too hot for plants (max 40°C)")
    print()
    
def test_temparature_input():
    check_temparture("25")
    check_temparture("abc")
    check_temparture("100")
    check_temparture("-50")
    print("all tests completed - program didn't crash")
    
if __name__ == "__main__":
    test_temparature_input()
    
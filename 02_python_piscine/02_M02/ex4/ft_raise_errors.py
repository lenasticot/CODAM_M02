def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        if not plant_name:
            raise ValueError(f"Plant name cannot be empty!")
        print(f"Plant '{plant_name}' is healthy")
    except ValueError as e:
        print(f"Error: {e}")
        
    try:
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        print(f"Water level is correct")
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        if sunlight_hours > 12 :
            raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)")
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
        print(f"Sunlight hour is correct")
    except ValueError as e:
        print(f"Error: {e}")
    
    print("")
    
def test_plant_checks():
    print("=== Garden Plant Health Checker ===")
    print("Testing good values...")
    check_plant_health("tomato", 5, 5)
    print("Testing empty plant name...")
    check_plant_health("", 5, 5)
    print("All error raising tests completed")
    print("Testing Sunlight hours")
    check_plant_health("tomato", 5, 1)
    check_plant_health("tomato", 5, 5)
    check_plant_health("tomato", 5, 15)
    print("Testing water level")
    check_plant_health("tomato", 5, 1)
    check_plant_health("tomato", 5, 5)
    check_plant_health("tomato", 5, 15)
    print("All error raising tests completed")
    
if __name__ == "__main__":
    test_plant_checks()
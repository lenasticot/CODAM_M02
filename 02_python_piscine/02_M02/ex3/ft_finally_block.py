def water_plants(plant_list):
    print("Opening watering system!")
    try:
        for plants in plant_list:
            if not isinstance(plants, str):
                raise ValueError(f"Cannot water '{plants}' - invalid plant!")
            print(f"Watering this plant: {plants}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system! (cleanup)")
        
            

def test_watering_system():
    print("Testing normal watering")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")
    print("\nTesting with error...")
    water_plants(["Tomato", 1, "carrots"])
    print("\nCleanup always happens, even with errors!")

if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
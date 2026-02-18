class GardenError(Exception):
    pass
class PlantError(GardenError):
    pass
class WaterError(GardenError):
    pass

def water_plant(amount):
    if amount < 5:
        raise WaterError("Not enough water in the tank!")

def check_plant(health):
    if health < 5:
        raise PlantError("The tomato plant is wilting!")

def raise_error():
    print("\nTesting WaterError...")
    try:
        water_plant(2)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nTesting PlantError")
    try:
       check_plant(2)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\nTesting catching all garden errors...")
    try:
        check_plant(2)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        water_plant(2)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    
    
    print("\nAll custom error types work correctly")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    raise_error()
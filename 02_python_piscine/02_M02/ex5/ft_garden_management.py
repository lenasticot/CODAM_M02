class GardenError(Exception):
    pass
class HealthError(GardenError):
    pass
class WaterError(GardenError):
    pass

class Plant():
	def __init__(self, name, water, sunlight):
		self.name = name
		self.water = water
		self.sunlight = sunlight

class GardenManager:
	_total_plants = 0
	def __init__(self):
		self.plant_list = []
	def add_plant(self, plant):
		try:
			if not isinstance(plant, Plant):
				raise TypeError("Must provide a Plant Object")
			if not plant.name:
				raise ValueError(f"plant name cannot be empty!")
			self.plant_list.append(plant)
			GardenManager._total_plants += 1
			print(f"Added {plant.name} successfully")
		except (ValueError, TypeError) as e:
			print(f"Error adding plant: {e}")
	def water_plant(self, water_plant):
		print("=== Opening watering system ===")
		try:
			if water_plant > 10:
				raise WaterError(f"Water level {water_plant} is too high (max 10)")
			if water_plant < 2:
				raise WaterError(f"Water level {water_plant} is too low (min 2)")
			for plant in self.plant_list:
				print(f"Watering {plant.name} - success")
				plant.water += water_plant
		except WaterError as e:
			print(f"Error: {e}")
		finally:
			print("Closing watering system (cleanup)")

	def check_plant(self):
		print("Checking plant health...")
		for plant in self.plant_list:
			errors = []
			try:
				if plant.water > 10:
					raise WaterError(f"Water level {plant.water} is too high (max 10)")
				if plant.water < 2:
					raise WaterError(f"Water level {plant.water} is too low (min 2)")
			except WaterError as e:
				errors.append(str(e))
			try: 
				if plant.sunlight > 10:
					raise HealthError(f"Sun level {plant.sunlight} is too high! (max 10)")
				if plant.sunlight < 2:
					raise HealthError(f"Sun level {plant.sunlight} is too low! (min 2)")
			except HealthError as e:
				errors.append(str(e))
			if errors:
				for error in errors:
					print(f"Error checking {plant.name}: {error}")
			else:
				print(f"{plant.name}: healthy (water: {plant.water}, sun: {plant.sunlight})")

def test_garden_management():
	print("=== Garden Management System ===\n")
	manager = GardenManager()
	print("Adding plants to garden...")
	tomato = Plant("Tomato", 5, 5)
	jonquille = Plant("Jonquille", 7, 10)
	lettuce = Plant("", 4, 5)

	manager.add_plant(tomato)
	print("\n=== Testing Error Recovery ===")
	manager.add_plant(lettuce)
	print("System sill working after error!")
	manager.add_plant(jonquille)

	print("")
	print("Watering Plants...")
	manager.water_plant(5)
	manager.water_plant(15)
	print("")
	manager.check_plant()

  
if __name__ == "__main__":
    test_garden_management()
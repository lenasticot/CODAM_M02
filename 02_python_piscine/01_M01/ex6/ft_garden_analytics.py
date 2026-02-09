"""Build a comprehensive garden data analytics platform that processes and analyzes garden data. This system needs to handle complex data relationships and provide detailed
analytics using nested components and inheritance chains."""

# add utility functions that don't need specific garden data
# show different types of methods: instance methods, class-level methods, and utility functions
# Each garden should track plant collections and statistics
# Use your nessted statistics helper to calculate analytics
# Organize everything wihtin appropriate structures - avoid scattered global functions

# need to 
	#
class GardenManager:
    """
	Can handle multiple gardens
	"""
    def __init__(self, garden):
        self.garden = garden
    def add_garden(self, garden):
         pass
    @classmethod
    def create_garden_network(cls):
         pass
    @classmethod
    def total_garden(cls):
         pass
    class GardenStats:
         """
         helper inside the manager for calculating statistics
         """
         @staticmethod
         def calculate_growth():
              pass
         @staticmethod
         def calculate_height():
              pass
         @staticmethod
         def plant_types():
              pass

            
             
        
class Garden():
    def __init__(self, owner):
        self.owner = owner
    def add_plant(self, plant):
        pass
    def all_plants_grow(self):
        pass
    def get_report(self):
        pass
    def calculate_score(self):
        pass
    
class Plant():
    """Add information about the plants here"""
    def __init__(self, name, age, height, type, color):
         self.name = name
         self.age = age
         self.height = height
         self.type = type
         self.color = color
    def get_height(self):
        return self._height
    def set_height(self, value):
        if value < 0:
            print(f"Invalid operation attempted height {value} [REJECTED]")
        else:
            self._height = value
    def get_age(self):
        return self._age
    def set_age(self, value):
        if value < 0:
            print(f"Invalid operation attempted age {value} [REJECTED]")
        else:
            self._age = value
    def grow(self, cm):
        pass
    def __str__(self):
        pass
        
    
         

class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        pass
    def bloom(self):
        pass
    def __str__(self):
        pass

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_point):
        pass
    def prize_point(self):
        pass
    def __str__(self):
        pass

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")



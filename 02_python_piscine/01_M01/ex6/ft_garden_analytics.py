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
    def add_garden(garden):
         pass
    @classmethod
    def create_garden_network():
         pass
    @classmethod
    def total_garden():
         pass
    class GardenStats:
         """
         helper inside the manager for calculating statistics
         """
         @staticmethod
         def calculate_growth(cls):
              pass
         @staticmethod
         def calculate_height(cls):
              pass
         @staticmethod
         def plant_types(cls):
              pass

            
             
        

class Plant():
    """Add information about the plants here"""
    def __init__(self, name, age, height, type, color):
         self.name = name
         self.age = age
         self.height = height
         self.type = type
         self.color = color
    def __str__(self):
         # need to add the person garden name 
         # so need to link the garden creator
         # and 
         return f"Added {self.name} to "
	
    
         

class FloweringPlant(Plant):
    pass

class PrizeFlower(Plant):
    pass

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

"""Class Garden Manager 
- Create the person
- Create the garden
	Class Garden Stats
     - class method: Display the different plants
      - class method: display the new added plants
       - class method: Display the types of new plants added
        - height validation test
          - class method: Garden scores
            - class method: Total gardens managed

Class Garden
- add plant to the total managed
- does the total from prize points?
	Class Plant
     - Define plant type, color, height...etc.
      - Static method : flowering plants
       - Static method: Prize flower"""


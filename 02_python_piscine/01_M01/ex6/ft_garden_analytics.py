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
        self.plants_list = []
        self.total_growth = 0

    def add_plant(self, plant):
        self.plants_list.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def all_plants_grow(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants_list:
            self.total_growth += 1
            plant.grow(1)
            print(f"{plant.name} grew 1 cm")

    def get_report(self):
        # Affiche "=== [owner]'s Garden Report ==="
        # Liste toutes les plantes avec leur __str__()
        # Affiche les stats (plants added, total growth, plant types)
        regular = 0
        flowering = 0
        prize_flower= 0
        print(f"=== {self.owner}'s Garden report ===")
        print("Plants in garden:")
        for plant in self.plants_list:
            print(f"- {plant}")
            if(isinstance(plant, PrizeFlower)):
                prize_flower += 1
            elif(isinstance(plant, FloweringPlant)):
                flowering += 1
            elif(isinstance(plant, Plant)):
                regular += 1
           
        print(f"\nPlants added: {len(self.plants_list)}, Total growth: {self.total_growth}")
        print(f"Plant types: {regular} regular, {flowering} flowering, {prize_flower} prize flowers")
    def calculate_score(self):
        score = 0
        for plant in self.plants_list:
            score += plant.get_height()
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        return score

#ok 
class Plant():
    def __init__(self, name, height):
         self.name = name
         self.height = height
    def get_height(self):
        return self._height

    def set_height(self, value):
        if value < 0:
            print(f"Invalid operation attempted height {value} [REJECTED]")
        else:
            self._height = value
    
    def grow(self, cm):
        if cm < 0:
            print("Invalid operation, need positive value to grow")
        else:
            self.height += cm
  
    def __str__(self):
        return f"{self.name} : {self.height} cm"
        
#ok    
class FloweringPlant(Plant):
    """To add on top of plant"""
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
    def __str__(self):
        return f"{self.name}: {self.height} cm, flowers (blooming)"

#ok
class PrizeFlower(FloweringPlant):
    """to add on top of flowering plant"""
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points
    def __str__(self):
        return f"{self.name}: {self.height} cm, flowers (blooming), Prize point: {self.points}"

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    alice_garden = Garden("Alice")
    oak_tree = Plant("Oak Tree", 101)
    rose = FloweringPlant("Rose", 26, "red")
    sunflower = PrizeFlower("Sunflower", 51, "yellow", 10)
    print(oak_tree)
    print(rose)
    print(sunflower)

    
    alice_garden.add_plant(oak_tree)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)
    alice_garden.all_plants_grow()
    alice_garden.get_report()




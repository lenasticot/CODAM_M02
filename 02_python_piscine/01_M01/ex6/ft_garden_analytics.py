class GardenManager:
    """Can handle multiple gardens"""
    _total_gardens = 0
    def __init__(self):
        self.garden_list = []
    def add_garden(self, garden):
        self.garden_list.append(garden)
        GardenManager._total_gardens += 1
        print(f"{garden.owner}'s garden has been created")
    @classmethod
    def create_garden_network(cls, owner_list):
         manager = GardenManager()
         for owner in owner_list:
             garden = Garden(owner)
             manager.add_garden(garden)   
         return manager
    @classmethod
    def total_garden(cls):
         return cls._total_gardens
    def print_scores(self):
        print(f"Garden scores - ", end="")
        for garden in self.garden_list:
            print(f"{garden.owner}: {garden.calculate_score()} ", end="")
        print()
    class GardenStats:
         """
         helper inside the manager for calculating statistics
         """
         @staticmethod
         def validate_height(plants_list):
            for plants in plants_list:
              if plants.height < 0:
                  return "false"
            return "true"
         @staticmethod
         def plant_types(plants_list):
             regular = 0
             flowering = 0
             prize_flower= 0
             for plant in plants_list:
                  if(isinstance(plant, PrizeFlower)):
                       prize_flower += 1
                  elif(isinstance(plant, FloweringPlant)):
                       flowering += 1
                  elif(isinstance(plant, Plant)):
                       regular += 1
             return regular, flowering, prize_flower
                  
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
        print(f"=== {self.owner}'s Garden report ===")
        print("Plants in garden:")
        for plant in self.plants_list:
            print(f"- {plant}")
        regular, flowering, prize_flower = GardenManager.GardenStats.plant_types(self.plants_list)
        print(f"Plants added: {len(self.plants_list)}, Total growth: {self.total_growth}")
        print(f"Plant types: {regular} regular, {flowering} flowering, {prize_flower} prize flowers")
    def calculate_score(self):
        score = 0
        for plant in self.plants_list:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.points
        return score

class Plant():
    def __init__(self, name, height):
         self.name = name
         self.height = height
    def grow(self, cm):
        if cm < 0:
            print("Invalid operation, need positive value to grow")
        else:
            self.height += cm
    def __str__(self):
        return f"{self.name} : {self.height} cm"
           
class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
    def __str__(self):
        return f"{self.name}: {self.height} cm, {self.color} flowers (blooming)"

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points
    def __str__(self):
        return f"{self.name}: {self.height} cm, {self.color} flowers (blooming), Prize point: {self.points}"

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    alice_garden = Garden("Alice")
    oak_tree = Plant("Oak Tree", 101)
    rose = FloweringPlant("Rose", 26, "red")
    sunflower = PrizeFlower("Sunflower", 51, "yellow", 10)
    print(oak_tree)
    print(rose)
    print(sunflower)
    bob_garden = Garden("Bob")
    tomato = PrizeFlower("tomato", 37, "red", 20)
    hibiscus = FloweringPlant("hibiscus", 54, "pink")
    
    manager = GardenManager()
    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)
    
    alice_garden.add_plant(oak_tree)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)
    alice_garden.all_plants_grow()
    alice_garden.get_report()
    alice_garden.calculate_score()
    bob_garden.add_plant(tomato)
    bob_garden.add_plant(hibiscus)
    bob_garden.all_plants_grow()
    bob_garden.get_report()
    bob_garden.calculate_score()
    manager.print_scores()
    print(f"Total gardens managed: {GardenManager.total_garden()}")
    NewManager = GardenManager.create_garden_network(["Jeanne", "Pierre"])



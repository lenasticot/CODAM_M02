class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age
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
    def __str__(self):
        return f"{self.name}: {self.get_height()}cm, {self.get_age()} days"
    
class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
    def bloom(self):
        return f"Rose is blooming beautifully!"
    def __str__(self):
        return f"{self.name} (Flower): {self.get_height()}cm, {self.get_age()} days, {self.color} color"

class Tree(Plant):
    def __init__(self, name, height, age, trunk):
        super().__init__(name, height, age)
        self.trunk = trunk
    def produce_shade(self):
        return f"Oak provides 78 square meters of shade"
    def __str__(self):
        return f"{self.name} (Tree): {self.get_height()}cm, {self.get_age()} days, {self.trunk}cm diameter"

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
    def nutritional_value(self):
        return f"Tomato is rich in vitamin C"
    def __str__(self):
        return f"{self.name} (Vegetable): {self.get_height()}cm, {self.get_age()} days, {self.harvest_season} harvest"

if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Tree", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer")
    
    print(rose)
    print(rose.bloom())
    print(oak)
    print(oak.produce_shade())
    print(tomato)
    print(tomato.nutritional_value())
    # print()
    # plants = [rose, oak, tomato]
    # for plant in plants:
    #     print(plant)
    #     if isinstance(plant, Flower):
    #         print(plant.bloom())
    #     elif isinstance(plant, Tree):
    #         print(plant.produce_shade())
    #     elif isinstance(plant, Vegetable):
    #         print(plant.nutritional_value())
    
    
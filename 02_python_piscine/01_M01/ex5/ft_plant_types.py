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
        return f"Current Plant: {self.name} ({self.get_height()} cm, {self.get_age()} days)"
    
class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
    def bloom(self):
        pass
    def __str__(self):
        parent_info = super().__str__()
        return f"{parent_info}, Color: {self.color}"

class Tree(Plant):
    def __init__(self, name, height, age, trunk):
        super().__init__(name, height, age)
        self.trunk = trunk
    def produce_shade(self):
        pass
    def __str__(self):
        parent_info = super().__str__()
        return f"{parent_info}, Trunk Diameter: {self.trunk}"

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    def __str__(self):
        parent_info = super().__str__()
        return f"{parent_info}, harvest season: {self.harvest_season}, nutritional value: {self.nutritional_value}"
  
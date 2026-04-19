from .creature_cards import Creature

class Flameling(Creature):
    def __init__(self):
        super().__init__("Flameling", "Fire")
    def attack(self):
        return f"{self.name} use Ember!"

class Pyrodon(Creature):
    def __init__(self):
        super().__init__("Pyrodon", "Fire/Flying")
    def attack(self):
        return f"{self.name} use Flamethrower!"

class Aquabub(Creature):
    def __init__(self):
        super().__init__("Aquabub", "Water")
    def attack(self):
        return f"{self.name} use Water Gun!"

class Torragon(Creature):
    def __init__(self):
        super().__init__("Torragon", "Water")
    def attack(self):
        return f"{self.name} use Hydro Pump!"
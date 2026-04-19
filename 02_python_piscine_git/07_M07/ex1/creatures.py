from .capability import HealCapability, TransformCapability
from ex0.creature_cards import Creature

class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")
    def attack(self):
        return f"{self.name} uses vine Whip!"
    def heal(self, target):
        if target == self.name:
            return f"{self.name} heals itself for a small amount"
        else:
            return f"{self.name} heals {target} for a small amount"

class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")
    def attack(self):
        return f"{self.name} uses Petal Dance!"
    def heal(self, target):
        if target == self.name:
            return f"{self.name} heals itself for a small amount"
        else:
            return f"{self.name} heals {target} for a small amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")
    def attack(self):
        if not self.transformed:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"
    def transform(self):
        if not self.transformed:
            self.transformed = True
            return f"{self.name} shifts into a sharper form"
        else:
            return f"{self.name} stabilizes its form"
    def revert(self):
        if self.transformed:
            self.transformed = False
            return f"{self.name} returns to normal"
        else:
            return f"{self.name} stabilizes its form"


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")
    def attack(self):
        if not self.transformed:
            return f"{self.name} attacks normally"
        else:
            return f"{self.name} unleashes a devastating morph strike!"
    def transform(self):
        if not self.transformed:
            self.transformed = True
            return f"{self.name} morphs into a dragonic battle form!"
        else:
            return f"{self.name} stabilizes its form"
    def revert(self):
        if self.transformed:
            self.transformed = False
            return f"{self.name} returns to normal"
        else:
            return f"{self.name} stabilizes its form"
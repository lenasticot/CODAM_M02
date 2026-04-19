from ex0.creature_factory import CreatureFactory
from .creatures import Shiftling, Morphagon, Sproutling, Bloomelle

class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        return Shiftling()
    def create_evolved(self):
        return Morphagon()

 
class HealingCreatureFactory(CreatureFactory):
    def create_base(self):
        return Sproutling()
    def create_evolved(self):
        return Bloomelle()
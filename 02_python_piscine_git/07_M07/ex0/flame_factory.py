from .creature_factory import CreatureFactory
from .creatures import Flameling, Pyrodon

class FlameFactory(CreatureFactory):
    def create_base(self):
        return Flameling()
    def create_evolved(self):
        return Pyrodon()
from .creature_factory import CreatureFactory
from .creatures import Flameling, Pyrodon


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()

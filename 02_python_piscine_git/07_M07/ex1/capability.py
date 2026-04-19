from abc import ABC, abstractmethod
from ex0.creature_cards import Creature
from ex0.creature_factory import CreatureFactory

class HealCapability(ABC):
    @abstractmethod
    def heal(self, target):
        pass


class TransformCapability(ABC):
    def __init__(self):
        super().__init__()
        self.transformed = False
    @abstractmethod
    def transform(self):
        pass
    @abstractmethod
    def revert(self):
        pass





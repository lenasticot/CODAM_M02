from abc import ABC, abstractmethod

class Creature(ABC):
    def __init__(self, name, race):
        super().__init__()
        self.name = name
        self.race = race
    @abstractmethod
    def attack(self):
        pass
    def describe(self):
        return f"{self.name} is a {self.race} type creature"

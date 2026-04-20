from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, race: str) -> None:
        super().__init__()
        self.name: str = name
        self.race: str = race

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.race} type creature"

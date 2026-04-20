from typing import Any

from .battleStrategy import BattleStrategy
from ex1.capability import HealCapability, TransformCapability


class NormalStrategy(BattleStrategy):
    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{type(creature).__name__}'"
                " for this Normal strategy"
                 )
        print(creature.attack())

    def is_valid(self, creature: Any) -> bool:
        return True


class AgressiveStrategy(BattleStrategy):
    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{type(creature).__name__}'"
                " for this Agressive strategy"
                )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())

    def is_valid(self, creature: Any) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        else:
            return False


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{type(creature).__name__}'"
                "for this Defensive strategy"
                )
        print(creature.attack())
        print(creature.heal())

    def is_valid(self, creature: Any) -> bool:
        if isinstance(creature, HealCapability):
            return True
        else:
            return False

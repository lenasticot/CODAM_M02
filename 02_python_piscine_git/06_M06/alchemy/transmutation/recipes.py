from ..elements import create_air
from alchemy.potions import strength_potion

from elements import create_fire  # type: ignore[import-untyped]
__all__ = ["lead_to_gold"]


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew {create_air()}"
        f"and {strength_potion()} mixed with '{create_fire()}'"
    )

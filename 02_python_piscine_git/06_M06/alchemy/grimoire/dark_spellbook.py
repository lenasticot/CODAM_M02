from .dark_validator import (
    dark_validate_ingredients,  # type: ignore[attr-defined]
)


def dark_spell_allowed_ingredients() -> list:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result = dark_validate_ingredients(ingredients)
    return f"Dark spell '{spell_name}' with ingredients {result}"

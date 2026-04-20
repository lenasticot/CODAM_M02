from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    allowed = dark_spell_allowed_ingredients()
    is_valid = any(item in ingredients.lower() for item in allowed)
    keyword = "VALID" if is_valid else "INVALID"
    return f"Ingredients '{ingredients}': {keyword}"

def validate_ingredients(ingredients: str):
    allowed = ["earth", "air", "fire", "water"]
    is_valid = any(item in ingredients.lower() for item in allowed)
    keyword = "VALID" if is_valid else "INVALID"
    return f"({ingredients} - {keyword})"

class SecurePlant:
    """Plant model that guards against invalid height/age values."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create a SecurePlant with initial values."""
        self.name: str = name
        self._height: int = height
        self._age: int = age

    def get_height(self) -> int:
        """Get the current height (cm)."""
        return self._height

    def set_height(self, value: int) -> None:
        """Update height if the value is non-negative."""
        if value < 0:
            print(f"Invalid operation attempted height {value} [REJECTED]")
        else:
            self._height = value

    def get_age(self) -> int:
        """Get the current age (days)."""
        return self._age

    def set_age(self, value: int) -> None:
        """Update age if the value is non-negative."""
        if value < 0:
            print(f"Invalid operation attempted age {value} [REJECTED]")
        else:
            self._age = value

    def __str__(self):
        return (
            f"Current Plant: {self.name}"
            f" ({self.get_height()} cm, {self.get_age()} days)"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    print(f"Plant created: {rose.name} ")
    print(f"Height updated: {rose.get_height()} cm [OK]")
    print(f"Age updated: {rose.get_age()} days [OK]")

    rose.set_height(-5)
    rose.set_age(-5)
    print(rose)

"""Garden plant hierarchy with type-safe methods and docstrings."""


class Plant:
    """Base class for garden plants."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant with its name, height (cm), and age (days)."""
        self.name: str = name
        self._height: int = height
        self._age: int = age

    def get_height(self) -> int:
        """Return the plant's height in cm."""
        return self._height

    def set_height(self, value: int) -> None:
        """Set height to a non-negative value, or reject invalid value."""
        if value < 0:
            print(f"Invalid operation attempted height {value} [REJECTED]")
        else:
            self._height = value

    def get_age(self) -> int:
        """Return the plant's age in days."""
        return self._age

    def set_age(self, value: int) -> None:
        """Set age to a non-negative value, or reject invalid value."""
        if value < 0:
            print(f"Invalid operation attempted age {value} [REJECTED]")
        else:
            self._age = value

    def __str__(self) -> str:
        return f"{self.name}: {self.get_height()}cm, {self.get_age()} days"


class Flower(Plant):
    """Flower type derived from Plant."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> str:
        """Return a bloom status string."""
        return f"{self.name} is blooming beautifully!"

    def __str__(self) -> str:
        return (
            f"{self.name} (Flower):"
            f"{self.get_height()}cm, {self.get_age()} days,"
            f"{self.color} color"
        )


class Tree(Plant):
    """Tree type derived from Plant."""

    def __init__(self, name: str, height: int, age: int, trunk: int) -> None:
        super().__init__(name, height, age)
        self.trunk: int = trunk

    def produce_shade(self) -> str:
        """Return a shade production status string."""
        return f"{self.name} provides 78 square meters of shade"

    def __str__(self) -> str:
        return (
            f"{self.name} (Tree): {self.get_height()}cm,"
            f"{self.get_age()} days, {self.trunk}cm diameter"
        )


class Vegetable(Plant):
    """Vegetable type derived from Plant."""

    def __init__(self, name: str, height: int,
                 age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season

    def nutritional_value(self) -> str:
        """Return a nutritional value string."""
        return f"{self.name} is rich in vitamin C"

    def __str__(self) -> str:
        return (
            f"{self.name} (Vegetable): {self.get_height()}cm,"
            f" {self.get_age()} days, {self.harvest_season} harvest"
        )


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 25, 42, "blue")
    oak = Tree("Oak", 500, 1825, 50)
    cedar = Tree("Cedar", 350, 3000, 20)
    tomato = Vegetable("Tomato", 80, 90, "summer")
    cucumber = Vegetable("Cucumber", 25, 50, "spring")

    print(rose)
    print(rose.bloom())
    print("")
    print(tulip)
    print(tulip.bloom())
    print("")
    print(oak)
    print(oak.produce_shade())
    print("")
    print(cedar)
    print(cedar.produce_shade())
    print("")
    print(tomato)
    print(tomato.nutritional_value())
    print("")
    print(cucumber)
    print(cucumber.nutritional_value())

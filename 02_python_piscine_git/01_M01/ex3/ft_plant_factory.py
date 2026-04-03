class Plant:
    """Represents a plant with name, height and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new Plant instance."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self, cm: int) -> None:
        """Increase the plant height in centimeters."""
        self.height += cm

    def time(self, duration: int) -> None:
        """Advance the plant age in days."""
        self.age += duration

    def __str__(self) -> str:
        return f"{self.name} ({self.height} cm, {self.age} days)"

    def get_info(self) -> None:
        """Print plant information to stdout."""
        print(self)


if __name__ == "__main__":

    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.name} ({plant.height} cm, {plant.age} days) ")
    print(f"\nTotal plants created: {len(plants)}")

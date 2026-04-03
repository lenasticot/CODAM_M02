class Plant:
    """Represents a growing garden plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create a Plant with a name, height (cm), and age (days)."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self, cm: int) -> None:
        """Increase plant height (cm)."""
        self.height += cm

    def time(self, duration: int) -> None:
        """Increase plant age (days)."""
        self.age += duration

    def __str__(self) -> str:
        return f"{self.name}: {self.height} cm, {self.age} days old"

    def get_info(self) -> None:
        """Print current plant information."""
        print(self)


if __name__ == "__main__":

    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Tulip", 40, 7)
    print("=== Day 1 ===")
    plant1.get_info()
    # plant2.get_info()
    day1_height = plant1.height
    grow = 6
    time = 6
    print("=== Day 7 ===")
    plant1.grow(grow)
    plant1.time(time)
    # plant2.grow(grow)
    # plant2.time(time)
    plant1.get_info()
    # plant2.get_info()
    print(f"Growth this week: +{grow}cm")
    # print(f"Growth this week for {plant2.name}: {grow}")

from typing import List


class GardenManager:
    """Manages multiple gardens and provides analytics."""
    _total_gardens: int = 0

    def __init__(self) -> None:
        """Initialize a new GardenManager with an empty list of gardens."""
        self.garden_list: List['Garden'] = []

    def add_garden(self, garden: 'Garden') -> None:
        """Add a garden to the manager and increment the total garden count.

        Args:
            garden: The Garden instance to add.
        """
        self.garden_list.append(garden)
        GardenManager._total_gardens += 1
        print(f"{garden.owner}'s garden has been created")

    @classmethod
    def create_garden_network(cls,
                              owner_list: List[str]) -> 'GardenManager':
        """Create a GardenManager and add gardens for each owner in the list.

        Args:
            owner_list: List of owner names for the gardens.

        Returns:
            A new GardenManager instance with gardens for each owner.
        """
        manager = GardenManager()
        for owner in owner_list:
            garden = Garden(owner)
            manager.add_garden(garden)
        return manager

    @classmethod
    def total_garden(cls) -> int:
        """Get the total number of gardens created across all managers.

        Returns:
            The total number of gardens.
        """
        return cls._total_gardens

    def print_scores(self) -> None:
        """Print the scores of all gardens managed by this manager."""
        print("Garden scores - ", end="")
        for i, garden in enumerate(self.garden_list):
            print(f"{garden.owner}: {garden.calculate_score()} ", end="")
            if i < len(self.garden_list) - 1:
                print(", ", end="")
        print()

    class GardenStats:
        """
        Helper class inside the manager for calculating statistics on plants.
        """
        @staticmethod
        def validate_height(plants_list: List['Plant']) -> bool:
            """Validate that all plants have non-negative height.

            Args:
                plants_list: List of Plant instances to validate.

            Returns:
                True if all plants have height >= 0, False otherwise.
            """
            for plants in plants_list:
                if plants.height < 0:
                    return False
            return True

        @staticmethod
        def plant_types(plants_list: list['Plant']) -> tuple[int, int, int]:
            """Count the number of each type of plant.

            Args:
                plants_list: List of Plant instances.

            Returns:
                A tuple of regular_count, flowering_count, prize_flower_count
            """
            regular = 0
            flowering = 0
            prize_flower = 0
            for plant in plants_list:
                if (isinstance(plant, PrizeFlower)):
                    prize_flower += 1
                elif (isinstance(plant, FloweringPlant)):
                    flowering += 1
                elif (isinstance(plant, Plant)):
                    regular += 1
            return regular, flowering, prize_flower


class Garden:
    """Represents a garden owned by someone, containing plants."""
    def __init__(self, owner: str) -> None:
        """Initialize a new garden for the given owner.

        Args:
            owner: The name of the garden owner.
        """
        self.owner: str = owner
        self.plants_list: List['Plant'] = []
        self.total_growth: int = 0

    def add_plant(self, plant: 'Plant') -> None:
        """Add a plant to the garden.

        Args:
            plant: The Plant instance to add.
        """
        self.plants_list.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def all_plants_grow(self) -> None:
        """Make plants in the garden grow by 1 cm and update total growth."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants_list:
            self.total_growth += 1
            plant.grow(1)
            print(f"{plant.name} grew 1 cm")

    def get_report(self) -> None:
        """Print a report of the garden's plants and statistics."""
        print(f"=== {self.owner}'s Garden report ===")
        print("Plants in garden:")
        for plant in self.plants_list:
            print(f"- {plant}")
        regular, flowering, prize_flower = (
            GardenManager.GardenStats.plant_types(self.plants_list)
        )
        print(
            f"Plants added: {len(self.plants_list)},"
            f" Total growth: {self.total_growth}"
            )
        print(
            f"Plant types: {regular} regular, {flowering} flowering,"
            f" {prize_flower} prize flowers"
            )

    def calculate_score(self) -> int:
        """Calculate score of garden based on plant heights and prize points.

        Returns:
            The total score.
        """
        score = 0
        for plant in self.plants_list:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.points
        return score


class Plant:
    """Represents a basic plant with name and height."""
    def __init__(self, name: str, height: int) -> None:
        """Initialize a new plant.

        Args:
            name: The name of the plant.
            height: The initial height of the plant in cm.
        """
        self.name: str = name
        self.height: int = height

    def grow(self, cm: int) -> None:
        """Grow the plant by the specified number of cm.

        Args:
            cm: The number of cm to grow. Must be positive.
        """
        if cm < 0:
            print("Invalid operation, need positive value to grow")
        else:
            self.height += cm

    def __str__(self) -> str:
        """Return a string representation of the plant.

        Returns:
            A string describing the plant.
        """
        return f"{self.name} : {self.height} cm"


class FloweringPlant(Plant):
    """Represents a flowering plant with color."""
    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize a new flowering plant.

        Args:
            name: The name of the plant.
            height: The initial height of the plant in cm.
            color: The color of the flowers.
        """
        super().__init__(name, height)
        self.color: str = color

    def __str__(self) -> str:
        """Return a string representation of the flowering plant.

        Returns:
            A string describing the plant.
        """
        return (
            f"{self.name}: {self.height} cm,"
            f" {self.color} flowers (blooming)"
        )


class PrizeFlower(FloweringPlant):
    """Represents a prize flower with additional points."""
    def __init__(self, name: str, height: int,
                 color: str, points: int) -> None:
        """Initialize a new prize flower.

        Args:
            name: The name of the plant.
            height: The initial height of the plant in cm.
            color: The color of the flowers.
            points: The prize points for this flower.
        """
        super().__init__(name, height, color)
        self.points: int = points

    def __str__(self) -> str:
        """Return a string representation of the prize flower.

        Returns:
            A string describing the plant.
        """
        return (
            f"{self.name}: {self.height} cm, {self.color} flowers (blooming),"
            f" Prize point: {self.points}"
        )


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    alice_garden = Garden("Alice")
    oak_tree = Plant("Oak Tree", 101)
    rose = FloweringPlant("Rose", 26, "red")
    sunflower = PrizeFlower("Sunflower", 51, "yellow", 10)
    print(oak_tree)
    print(rose)
    print(sunflower)
    bob_garden = Garden("Bob")
    tomato = PrizeFlower("tomato", 37, "red", 20)
    hibiscus = FloweringPlant("hibiscus", 54, "pink")

    manager = GardenManager()
    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    alice_garden.add_plant(oak_tree)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)
    alice_garden.all_plants_grow()
    alice_garden.get_report()
    alice_garden.calculate_score()
    bob_garden.add_plant(tomato)
    bob_garden.add_plant(hibiscus)
    bob_garden.all_plants_grow()
    bob_garden.get_report()
    bob_garden.calculate_score()
    manager.print_scores()
    print(f"Total gardens managed: {GardenManager.total_garden()}")
    NewManager = GardenManager.create_garden_network(["Jeanne", "Pierre"])

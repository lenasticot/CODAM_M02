class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def grow(self, cm: int):
        self.height += cm
    def time(self, duration: int):
        self.age += duration
    def __str__(self):
        return f"{self.name}: {self.height} cm, {self.age} days old"
        
		

if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(plant1)
    day1_height = plant1.height
    print("=== Day 7 ===")
    plant1.grow(6)
    plant1.time(6)
    print(plant1)
    print(f"Growth this week: {plant1.height - day1_height}")
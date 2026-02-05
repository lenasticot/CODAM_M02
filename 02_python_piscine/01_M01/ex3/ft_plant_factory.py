class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def __str__(self):
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"
    

if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    for i in range(len(plants)):
        print(f"{plants[i]}")
    print(f"Total plants created: {i +1}")
    
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        
if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose:", "25cm,", "30 days old")
    plant2 = Plant("Sunflower:", "80cm,", "45 days old")
    plant3 = Plant("Cactus:", "15cm,", "120 days old")
    print(plant1.name, plant1.height, plant1.age)
    print(plant2.name, plant2.height, plant2.age)
    print(plant3.name, plant3.height, plant3.age)
    
    
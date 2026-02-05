class SecurePlant():
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age
    def get_height(self):
        return self._height
    def set_height(self, value):
        if value < 0:
            print(f"Invalid operation attempted height {value} [REJECTED]")
        else:
            self._height = value
    def get_age(self):
        return self._age
    def set_age(self, value):
        if value < 0:
            print(f"Invalid operation attempted age {value} [REJECTED]")
        else:
            self._age = value
    def __str__(self):
        return f"Current Plant: {self.name} ({self.get_height()} cm, {self.get_age()} days)"

if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    print(f"Plant created: {rose.name} ")
    print(f"Height updated: {rose.get_height()} cm [OK]")
    print(f"Age updated: {rose.get_age()} days [OK]")
    
    rose.set_height(-5)
    print(rose)
    
    
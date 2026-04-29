from typing import Callable

def mage_counter() -> Callable:
    x = 0
    def counting():
        nonlocal x
        x +=1
        return x
    return counting

def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power
    def power_accumulator(amount: int):
        nonlocal power
        power += amount
        return power
    return power_accumulator

def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item_name):
        return f"{enchantment_type} {item_name}"
    return enchantment

def memory_vault() -> dict[str, Callable]:
    storage = {}
    def store(key, value):
        storage[key] = value
    def recall(key):
        if key not in storage:
            return "Memory not found"
        else:
            return storage[key]
    return {
        "store": store,
        "recall": recall
        }


def main():
    y = mage_counter()
    for r in range(0, 3):
        print(y())
    
    power = spell_accumulator(50)
    for x in range(0, 3):
        print(f"new power: {power(10)}")
    
    sort = enchantment_factory("flaming")
    print(f"{sort("sword")}")
    
    # memory vault tests
    vault = memory_vault()

    vault["store"]("sword", "Excalibur")
    vault["store"]("spell", "Fireball")
    
    vault["recall"]("sword") 
    vault["recall"]("spell")
    vault["recall"]("shield") 
main()
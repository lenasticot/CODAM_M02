from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul

def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(add, spells)
    elif operation == "multiply":
        return reduce(mul, spells)
    elif operation == "max":
        return reduce(lambda a, b: a if a > b else b, spells)
    elif operation == "min":
        return reduce(lambda a, b: a if a < b else b, spells)
    else:
        raise ValueError(f"Unknown operation: {operation}")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
            "fire":  partial(base_enchantment, power = 50, element = "fire"),
            "shadow": partial(base_enchantment, power = 50, element = "shadow"),
            "lightning": partial(base_enchantment, power = 50, element = "lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <=1:
        return n
    return memoized_fibonacci(n -1) + memoized_fibonacci(n - 2)



def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(arg):
        return "Unknown spell type"
    
    @spell.register(int)
    def _(arg):
        return f"Damage spell hits for {arg}"
        
    @spell.register(str)
    def _(arg):
        return f"Enchantment: {arg}"
    
    @spell.register(list)
    def _(arg):
        return f"Multi-cast: {arg}"
    return spell

def main():
    print(spell_reducer([10, 20, 30], "add"))       
    print(spell_reducer([2, 3, 4], "multiply"))     
    print(spell_reducer([10, 50, 30], "max"))    
    print(spell_reducer([10, 50, 30], "min"))
    
    dispatch = spell_dispatcher()
    print(dispatch(50)) 
    print(dispatch("Fireball"))   
    print(dispatch([1, 2, 3]))  
    print(dispatch(3.14))
    
main()
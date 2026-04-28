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


@singledispatch
def spell_dispatcher() -> Callable[[Any], str]:
    pass

def main():
    spell_reducer([10, 20, 30], "add")       
    spell_reducer([2, 3, 4], "multiply")     
    spell_reducer([10, 50, 30], "max")       
    spell_reducer([10, 50, 30], "min")            
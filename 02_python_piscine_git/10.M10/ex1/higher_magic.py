from typing import Callable

def fire(target: str, power: int) -> str:
    return f"{target} is hit with fire and loose {power} points"

def water(target: str, power: int)-> str:
    return f"{target} is being attacked with water. -{power} points"

def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int):
        return (spell1(target, power)), spell2(target, power)
    return combined

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def new_spell(target: str, power: int):
        return base_spell(target, power * multiplier)
    return new_spell

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int):
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return conditional_spell

def spell_sequence(spells: list[Callable]) -> Callable:
    def order(target: str, power: int):
        result = []
        for spell in spells:
            result.append(spell(target, power))
        return result
    return order
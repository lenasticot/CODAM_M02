from typing import Callable
from functools import wraps
import time

def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper
        

def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(power, *args, **kwargs):
            if power < min_power:
                return "Insufficient power for this spell"
            return func(power, *args, **kwargs)
        return wrapper
    return decorator

def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)  # success → return immediately
                except Exception:
                    print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator

class MageGuild():
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(min_power=10)
        def _cast(power):
            return f"Successfully cast {spell_name} with {power} power"
        return _cast(power)


def main():
    # spell_timer
    print("testing spell timer...")
    @spell_timer
    def fireball(target):
        time.sleep(0.5)
        return f"Fireball hits {target}"
    
    print(fireball("Dragon"))
    print()

    # power_validator
    @power_validator(min_power=50)
    def thunder(power):
        return f"Thunder strikes for {power}"

    print(thunder(80))
    print(thunder(20))   
    print()

    # retry_spell
    print("Testing retrying spell...")
    attempts = [0]

    @retry_spell(max_attempts=3)
    def unstable_spell():
        attempts[0] += 1
        if attempts[0] < 3:
            raise Exception("Spell fizzled!")
        return "Spell succeeded!"

    print(unstable_spell())
    print()

    # MageGuild
    print("Tesint MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Zara"))   
    print(MageGuild.validate_mage_name("Z"))      
    print(guild.cast_spell("Fireball", 80))
    print(guild.cast_spell("Fireball", 5))        

main()
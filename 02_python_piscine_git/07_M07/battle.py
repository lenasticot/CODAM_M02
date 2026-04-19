from ex0 import FlameFactory, AquaFactory, CreatureFactory


def creatures_fight(fighter1, fighter2):
    print(f"{fighter1.describe()} vs. {fighter2.describe()}")
    print("fight!")
    print(fighter1.attack())
    print(fighter2.attack())


def creating_creatures(factory: CreatureFactory):
    try:
        base = factory.create_base()
        ev = factory.create_evolved()
        print(base.describe())
        print(base.attack())
        print(ev.describe())
        print(ev.attack())
        return base, ev
    except Exception as e:
        print(f"Factory failed: {e}")
        raise
        

def main():
    flame = FlameFactory()
    water = AquaFactory()
    print("Testing factory")
    flam, pyro = creating_creatures(flame)
    print()
    print("Testing factory")
    aqu, torr = creating_creatures(water)
    print()
    print("Testing battle")
    creatures_fight(flam, aqu)

main()

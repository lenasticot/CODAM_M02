from ex1.factories import TransformCreatureFactory, HealingCreatureFactory


def healing_factory():
    h = HealingCreatureFactory()
    base = h.create_base()
    evo = h.create_evolved()
    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print()
    print("evolved:")
    print(evo.describe())
    print(evo.attack())
    print(evo.heal())


def transform_factory():
    t = TransformCreatureFactory()
    base = t.create_base()
    evo = t.create_evolved()
    print("base")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print()
    print("evolved")
    print(evo.describe())
    print(evo.attack())
    print(evo.transform())
    print(evo.attack())
    print(evo.revert())


def main():
    print("Testing Creature with healing capability")
    healing_factory()
    print()
    print("Testing Creature with transform capability")
    transform_factory()


main()

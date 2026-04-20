from ex0 import FlameFactory, AquaFactory
from ex1.factories import TransformCreatureFactory, HealingCreatureFactory
from ex2.strategies import DefensiveStrategy, AgressiveStrategy, NormalStrategy


def battle(opponents: list):
    print("*** tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()
    opps = []
    for factory, strat in opponents:
        creature = factory.create_base()
        opps.append((creature, strat))
    for i in range(len(opps)):
        for j in range(i+1, len(opps)):
            print("* Battle * ")
            creature_i, strat_i = opps[i]
            creature_j, strat_j = opps[j]
            print(creature_i.describe())
            print("vs.")
            print(creature_j.describe())
            print()
            print("Now fight!")
            try:
                strat_i.act(creature_i)
            except ValueError as e:
                print(e)
            try:
                strat_j.act(creature_j)
            except ValueError as e:
                print(e)
            print()


def main():
    # initiating factories
    transform = TransformCreatureFactory()
    heal = HealingCreatureFactory()
    fire = FlameFactory()
    water = AquaFactory()
    # initiating strategies
    nor = NormalStrategy()
    agg = AgressiveStrategy()
    defe = DefensiveStrategy()
    print("=== Trying regular fight ===")
    battle([(heal, nor), (fire, nor)])
    print()
    print("=== Trying with wrong strategy ===")
    battle([(heal, agg), (fire, nor)])
    print()
    print("=== Trying with wrong strategy again ===")
    battle([(fire, agg), (water, defe)])
    print()
    print("=== Trying with other strategies ===")
    battle([(heal, defe), (transform, agg)])
    print()
    print("=== Trying with multiples opponenents ===")
    battle([(heal, nor), (fire, nor), (heal, defe), (transform, agg)])


main()

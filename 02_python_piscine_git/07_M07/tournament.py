from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1.factories import TransformCreatureFactory, HealingCreatureFactory
from ex2.strategies import DefensiveStrategy, AgressiveStrategy, NormalStrategy


def battle(opponents: list):

        
    print("*** tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()
    print("* Battle * ")
    #for opps in opponents:
    #    print(opps.describe())
    #    print("vs.")
    print("now fight!")
    for factory, strat in opponents:
        try:
            creature = factory.create_base()
            print(creature.describe())
            strat.act(creature)
            print()
        except ValueError as e:
            print(e)
    
    
def main():
    #initiating factories
    transform = TransformCreatureFactory()
    heal = HealingCreatureFactory()
    fire = FlameFactory()
    water = AquaFactory()
    #creating transform creatures
    base = transform.create_base()
    evo = transform.create_evolved()
    #creating healing creatures
    h = HealingCreatureFactory()
    base2 = h.create_base()
    evo2 = h.create_evolved()
    #creating other creatures
    nor = NormalStrategy()
    agg = AgressiveStrategy()
    defe = DefensiveStrategy()
    
    battle([(transform, agg), (fire, nor)])



    #agg.act(base)
    #defe.act(base)
    
main()
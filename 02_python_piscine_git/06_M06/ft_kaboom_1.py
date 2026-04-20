def main():
    print("=== Kaboom 1 ===")
    try:
        from alchemy.grimoire import dark_spellbook
        print(dark_spellbook.dark_spell_record("Camembert", "bats and frogs"))
    except ImportError:
        print("Not working")


main()

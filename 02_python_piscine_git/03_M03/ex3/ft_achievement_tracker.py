

def achievement_analytics(alice, bob, charlie):
    print("\n=== Achievement Analytics === ")
    unique_ach = alice | bob | charlie
    alice_ach = alice.difference(bob, charlie)
    bob_ach = bob.difference(alice, charlie)
    charlie_ach = charlie.difference(bob, alice)
    rare_ach = alice_ach | bob_ach | charlie_ach
    print(f"All unique achievements: {unique_ach}")
    print(f"Total unique achievements: {len(unique_ach)}")
    print("")
    print(f"Common to all player {alice & bob & charlie}")
    print(f"Rare achievements: {rare_ach}\n")
    print(f"Alice vs Bob Common: {alice & bob}")
    print(f"Alice unique: {alice_ach}")
    print(f"Bob unique: {bob_ach}")


def achievement_hunter():
    print("=== Achievement Tracker System ===\n")
    player_1 = "alice"
    player_2 = "bob"
    player_3 = "charlie"
    alice = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon",
        "boss_lady"
    }
    bob = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector"
    }
    charlie = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist"
    }
    print(f"Player {player_1} achievements: {alice}")
    print(f"Player {player_2} achievements: {bob}")
    print(f"Player {player_3} achievements: {charlie}")
    achievement_analytics(alice, bob, charlie)


achievement_hunter()

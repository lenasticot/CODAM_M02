# Your Mission: Create an Achievement Hunter using sets—the perfect tool for handling
# unique collections. No duplicates allowed in the hall of fame!
# What makes this epic:
# • Track unique achievements (no "First Kill" counted twice!)
# • Find achievements shared by multiple players (the "common ground")
# • Spot the ultra-rare achievements (bragging rights material!)
# • See who’s missing what achievements (gotta catch ’em all!)
# • Build player communities based on shared accomplishments

def achievement_analytics(alice, bob, charlie):
	print("=== Achievement Analytics === \n")
	unique_achievements = alice | bob | charlie
	alice_achievements = alice.difference(bob, charlie)
	bob_achievements = bob.difference(alice, charlie)
	charlie_achievements = charlie.difference(bob, alice)
	rare_achievements = alice_achievements | bob_achievements | charlie_achievements
	#problem level 10 is here for some reason?
	print(f"All unique achievements: {unique_achievements}")
	print(f"Total unique achievements: {len(unique_achievements)}")
	print("")
	print(f"Common to all player {alice & bob & charlie}")
	print(f"Rare achievements: {rare_achievements}")
	print(f"Alice vs Bob Common: {alice & bob}")
	print(f"Alice unique: {alice_achievements}")
	print(f"Bob unique: {bob_achievements}")


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

if __name__ == "__main__":
	achievement_hunter()
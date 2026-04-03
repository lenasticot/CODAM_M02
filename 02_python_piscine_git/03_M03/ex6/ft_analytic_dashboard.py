players = ["alice", "bob", "charlie", "diana"]
scores = [2300, 1800, 2150, 2050]
achievements = {
    "alice": ["first_kill", "level_10", "quest_complete", "treasure_hunter"],
    "bob": ["speed_run", "level_5", "quest_complete"],
    "charlie": [
        "level_5",
        "boss_slayer",
        "quest_complete",
        "treasure_hunter",
        "arena_champion",
        "speed_run",
    ],
    "diana": ["treasure_hunter", "arena_champion", "quest_complete"],
}
active = {"alice": True, "bob": True, "charlie": True, "diana": False}
regions = ["north", "east", "central", "north"]


def list_comprehension():
    print("=== List Comprehension Examples ===")
    high_score = [player for player,
                  score in zip(players, scores) if score > 2000]
    print(f"High scorers (>2000): {high_score}")
    double_score = [score * 2 for score in scores]
    print(f"Scores doubled: {double_score}")

    active_players = [player for player in active if active[player]]
    print(f"Active players: {active_players}")


def dict_comprehension():
    print("\n=== Dict Comprehension Examples ===")
    result = {player: score for player, score in zip(players, scores)}
    print(f"Player scores: {result}")
    value = {
        "high": len([score for score in scores if score > 2000]),
        "medium": len([score for score
                       in scores
                       if score < 2000 and score > 1500]),
        "low": len([score for score in scores if score < 1500])
        }
    print(f"Score categories: {value}")
    ach = {name: len(achievement)
           for name, achievement
           in achievements.items()}
    print(f"Achievement counts: {ach}")


def set_comprehension():
    print("\n=== Set Comprehension Examples ===")
    unique_player = {player for player in players}
    print(f"Unique players: {unique_player}")
    unique_achievement = {achievement for achievement_list
                          in achievements.values()
                          for achievement in achievement_list}
    print(f"Unique achievements: {unique_achievement}")
    unique_region = {region for region in regions}
    print(f"Active regions: {unique_region}")


def combined_analysis():
    print("\n=== Combined Analysis ===")
    unique_player = {player for player in players}
    print(f"Total player: {len(unique_player)}")
    unique_achievement = {achievement for achievement_list
                          in achievements.values()
                          for achievement in achievement_list}
    print(f"Total Unique Achievements: {len(unique_achievement)}")
    print(f"Average score: {sum(scores) / len(scores):.1f}")

    top_score, top_name = max(zip(scores, players))
    top_achievements = len(achievements[top_name])
    print(
        f"Top performer {top_name}: "
        f"{top_score} points, {top_achievements} achievements"
          )


def main():
    print("===Game Analytics Dashborard ===\n")
    list_comprehension()
    dict_comprehension()
    set_comprehension()
    combined_analysis()


main()

import sys


def parsing(str):
    coords = str.split(" ")
    try:
        for c in coords:
            score_list = list(int(c) for c in coords)
    except ValueError:
        print(f"Oupsi you typed {c}")
        return
    return score_list


def score_analytics():
    print("=== Player Score Analytics ===")
    int_scores = []
    if len(sys.argv) == 2:
        int_scores = parsing(sys.argv[1])
    else:
        for score in sys.argv[1:]:
            try:
                int_scores.append(int(score))
            except ValueError:
                print(f"Oupsi you typed {score} instead of a number")
                return
    if not int_scores:
        print(
            "No scores provided. "
            "Usage python3 ft_score_analytics.py <score1> <score2>...\n"
            "Or '<score1> <score2> <score3>' "
            )
        return
    print(f"Scores processed: {int_scores}")
    print(f"Total players: {len(int_scores)}")
    print(f"Total score: {sum(int_scores)}")
    print(f"Average score: {sum(int_scores) / len(int_scores):.1f}")
    print(f"High score: {max(int_scores)}")
    print(f"Low score: {min(int_scores)}")
    print(f"Score range: {max(int_scores) - min(int_scores)}")


score_analytics()

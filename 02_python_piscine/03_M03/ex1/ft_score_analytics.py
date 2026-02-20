import sys

# • Accept player scores from the command line (like cheat codes, but legal!)
# • Use lists to store and organize the scores
# • Calculate some basic stats that would make any game dev happy
# • Handle the "oops, I typed ’banana’ instead of ’1000’" scenarios gracefully
# • Make the output look cool enough to impress your gaming buddies

def score_analytics():
	int_scores = []
	for score in sys.argv[1:]:
		try:
				int_scores.append(int(score))
		except ValueError:
				print(f"Oupsi you typed {score} instead of a number")
				return	
	if not int_scores:
		print("No scores provided.")
		return
	
	print(f"Scores processed: {int_scores}")
	print(f"Total players: {len(int_scores)}")
	print(f"Total score: {sum(int_scores)}")
	print(f"Average score: {sum(int_scores) / len(int_scores):.1f}")
	print(f"High score: {max(int_scores)}")
	print(f"Low score: {min(int_scores)}")
	#what does the range do??
	print(f"Score range: {max(int_scores) - min(int_scores)}")

if __name__ == "__main__":
	print("=== Player Score Analytics ===")
	score_analytics()
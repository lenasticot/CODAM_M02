# Build a simple command interpreter that shows you’ve mastered the art
# of receiving external data. Think of it like learning to read quest scrolls that players send
# to your game!
import sys

def command_analysis():
	if len(sys.argv) == 1:
		print("No arguments provided!")
	print(f"Program name: {sys.argv[0]}")
	if len(sys.argv) > 1:
		print(f"Arguments received: {len(sys.argv) -1}")
		i = 2
		for args in sys.argv[1:]:
			print(f"Argument {i -1}: {args}")
			i += 1
	print(f"Total arguments: {len(sys.argv)}")

if __name__ == "__main__":
	print("=== Command quest ===")
	command_analysis()
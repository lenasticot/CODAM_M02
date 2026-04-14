# will use the from ... import ... structure to access alchemy/elements.py
# directly and then create air
from alchemy import elements

def main():
	print("=== Alembic 3 ===")
	print("Acessing alchemy/elements.py using 'from ... import ...' structure")
	print(f"Testing create_air: {elements.create_air()}")

main()

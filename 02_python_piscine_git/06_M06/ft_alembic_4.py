# will use import alchemy to access the alchemy module and then 
# create air. the create_earth() function will not be exposed through
# the module interface and raise and exception when called
# (you can catch the exception or not, the is only for pedagogical purposes)
# A mypy error will also raise, again, on purpose

import alchemy

def main():
	print("=== Alembic 4 ===")
	print("Accessing the alchemy module using 'import alchemy'")
	print(f"Testing create_air: {alchemy.create_air()}")
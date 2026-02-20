import sys, math

def check_error():
	int_coordinates = []
	# the error management must be different because it must display all the wrong data provided
	for coord in sys.argv[1:]:
		try:
				int_coordinates.append(int(coord))
		except ValueError:
				print(f"Oupsi you typed {coord} instead of a number")
				return	
	if not int_coordinates:
		print("No coordinates provided.")
		return
	create_tuple(int_coordinates)


def create_tuple(int_coordinates):
	tuple_coordinates = tuple(int_coordinates)
	print(f"Parsing coordinates: {tuple_coordinates}")
	print("In my tuple there is:")
	i = 0
	for nbr in tuple_coordinates:
		print(f"{nbr}")
	print(f"Parsing coordinates: ")
	x, y, z = tuple_coordinates
	print(f"Parsed position: ({x}, {y}, {z})")

def distance_caculation(x, y, z):
	math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

def demonstration(x, y, z):
	pass

if __name__ == "__main__":
	print("=== Game Coordinate System ===")
	check_error()

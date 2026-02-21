import sys, math

def parsing(str):
	print(f"Parsing coordinates: '{str}'")
	coords = str.split(",")
	try:
		coord_tuple = tuple(int(c) for c in coords)
	except ValueError as e:
		print(f"Error parsing coordinates: {e}")
		print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
		return
	print(f"Parsed position: {coord_tuple}")
	return coord_tuple

   
def check_error():
	coord_tuple = None
	if len(sys.argv) == 2:
		coord_tuple = parsing(sys.argv[1])
		if coord_tuple is None:
			return
	elif len(sys.argv) == 4:
		coords = sys.argv[1:]
		try:
			coord_tuple = tuple(int(c) for c in coords)
		except ValueError as e:
			print(f"Error parsing coordinates: {e}")
			print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
			return
		print(f"Position created: {coord_tuple}")
	else:
		print(f"The format and/or number of argument is wrong: {len(sys.argv)}, please provide a string of 3 integer or 3 integers")
	
	if len(coord_tuple) != 3:
		print(f"Error, excepted 3 coordinates, got {len(coord_tuple)}")
		return

	x, y, z = coord_tuple
	distance_caculation(x, y, z)
	demonstration(x, y, z)

def distance_caculation(x2, y2, z2):
	x1, y1, z1 = 0, 0, 0
	distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
	print(f"Distance between ({x1}, {y1}, {z1}) and ({x2}, {y2}, {z2}): {distance:.2f}")
	

def demonstration(x, y, z):
	print("\nUnpacking demonstration:")
	print(f"Player at x={x}, y={y}, z={z}")
	print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
	print("=== Game Coordinate System ===\n")
	if len(sys.argv) > 1:
		check_error()
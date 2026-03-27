import sys
import math
#to check when only 1 coordinate as ""
    #maybe to put as a proper try/expect

#ok need to work on the parsing might be a bit weak


def parsing(str):
    print(f"Parsing coordinates: '{str}'...")
    coords = str.split(",")
    try:
        for c in coords:
            coord_tuple = tuple(int(c) for c in coords)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return
    if len(coord_tuple) != 3:
        print("Error: expected 3 coordinates")
        return
    print(f"Parsed position: {coord_tuple}")
    return coord_tuple


def check_error():
    if len(sys.argv) > 1:
        print("=== Game Coordinate System ===\n")
    else:
        print(
            "No coordinates provided. "
            "Usage python3 ft_coordinate_system.py <coord1> <coord2>"
            )
        return
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
        print(
            f"The format and/or number of argument is wrong: {len(sys.argv)},"
            " please provide a string of 3 integer or 3 integers"
            )

    if len(coord_tuple) != 3:
        print(f"Error, excepted 3 coordinates, got {len(coord_tuple)}")
        return

    x, y, z = coord_tuple
    distance_caculation(x, y, z)
    demonstration(x, y, z)


def distance_caculation(x2, y2, z2):
    x1, y1, z1 = 0, 0, 0
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(
        f"Distance between ({x1}, {y1}, {z1}"
        f" and ({x2}, {y2}, {z2}): {distance:.2f}"
        )


def demonstration(x, y, z):
    print("\nUnpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


check_error()

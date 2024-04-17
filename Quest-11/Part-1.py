import sys
from itertools import combinations

def main(file_name):
    lines = read_file(file_name)
    map = flip(expand(flip(expand(lines))))
    galaxy_coords = get_galaxy_coord(map)
    galaxy_distance = get_galaxy_comb(galaxy_coords)

    print(sum(galaxy_distance))

def read_file(name):
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.read().splitlines()

def expand(lines):
    map = []

    for row in lines:
        if "#" not in row:
            map.append(row)
        map.append(row)

    return map

def flip(lines):
    map = []

    for col in range(0, len(lines[0])):
        new_line = ""

        for line in lines:
            new_line += (line[col])

        map.append(new_line)

    return map

def get_galaxy_coord(lines):
    return [(y, x) for y, line in enumerate(lines)  for x, el in enumerate(line) if el == "#"]

def get_galaxy_comb(galaxy_coords):
    return [distance(galaxy_1, galaxy_2) for galaxy_1, galaxy_2 in combinations(galaxy_coords, 2)]


def distance(galaxy_1, galaxy_2):
    """
    >>> distance((0, 3), (1, 7))
    5
    >>> distance((0, 3), (1, 3))
    1
    >>> distance((1, 7), (0, 3))
    5
    """
    y1, x1 = galaxy_1
    y2, x2 = galaxy_2
    dist = abs(y1 - y2) + abs(x2 - x1)

    return dist


if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-11/input.txt"
    main(file_name)

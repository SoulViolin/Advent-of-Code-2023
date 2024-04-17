import sys
import math
from itertools import combinations

def main(file_name):
    lines = read_file(file_name)
    galaxy_coords = get_galaxy_coord(lines)

    # Получаем количество пустых строк и флаги пустых столбцов
    empty_lines, empty_columns = count_empty_lines_columns(lines)

    galaxy_distance = get_galaxy_comb(galaxy_coords, empty_lines, empty_columns)

    print(sum(galaxy_distance))

def read_file(name):
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.read().splitlines()

def get_galaxy_coord(lines):
    return [(y, x) for y, line in enumerate(lines)  for x, el in enumerate(line) if el == "#"]

def get_galaxy_comb(galaxy_coords, empty_lines, empty_columns):
    return [distance(galaxy_1, galaxy_2, empty_lines, empty_columns) for galaxy_1, galaxy_2 in combinations(galaxy_coords, 2)]

def distance(galaxy_1, galaxy_2, empty_lines, empty_columns):
    """
    # >>> distance((0, 3), (1, 7), [False, False, False, True, False, False, False, True, False, False], [False, False, True, False, False, True, False, False, True, False])
    >>> distance((0, 0), (0, 1), [], [False, False, True])
    1
    >>> distance((0, 0), (0, 2), [], [False, True, False])
    4

    # #..
    # .#.
    # ...
    >>> distance((0, 0), (1, 1), [False, False, True], [False, True, False])
    2

    # #..
    # ...
    # ..#
    >>> distance((0, 0), (2, 2), [False, True, False], [False, True, False])
    8
    """

    y1, x1 = galaxy_1
    y2, x2 = galaxy_2

    expancion = 1000000

    dist = abs(y1 - y2) + abs(x1 - x2)

    for is_empty in empty_lines[min(y1, y2):max(y1, y2)]:
        if is_empty:
            dist += expancion -1

    for is_empty in empty_columns[min(x1, x2):max(x1, x2)]:
        if is_empty:
            dist += expancion - 1

    return dist

def count_empty_lines_columns(lines):
    """
    >>> count_empty_lines_columns(['...#......', '.......#..', '#.........', '..........', '......#...', '.#........', '.........#', '..........', '.......#..', '#...#.....'])
    ([False, False, False, True, False, False, False, True, False, False], [False, False, True, False, False, True, False, False, True, False])
    """

    empty_lines = [True] * len(lines)

    empty_columns = [True] * len(lines[0])

    for i, line in enumerate(lines):
        if all(char == '.' for char in line):
            empty_lines[i] = True
        else:
            empty_lines[i] = False

        for idx, char in enumerate(line):
            if char != '.':
                empty_columns[idx] = False

    return empty_lines, empty_columns

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-11/input.txt"
    main(file_name)

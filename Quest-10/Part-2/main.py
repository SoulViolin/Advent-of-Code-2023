import sys

def main(file_name):
    lines = read_file(file_name)
    start = find_start(lines)
    area = find_area(lines, start)
    print(area)

def read_file(name):
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.readlines()

def find_start(lines):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == 'S':  # Начальная точка
                return (y, x)

def find_area(lines, start):
    """
    >>> find_route(['..F7.\n', '.FJ|.\n', 'SJ.L7\n', '|F--J\n', 'LJ...\n'], (0, 2))
    """
    visited = set()
    vertices_l = []
    vertices_r = []
    pos = get_start(start, lines)

    while pos != start:
        visited.add(pos)
        # print(visited)
        pos, points_l, points_r = get_direction(pos, lines, visited)
        # print(pos, points_l, points_r)
        vertices_l += points_l
        vertices_r += points_r
        # print_map(lines, pos)
        # input()

    area_1 = area(vertices_l)
    area_2 = area(vertices_r)

    return min(area_1, area_2)

def area(vertices):
    n = len(vertices)
    total_area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        total_area += (x1 * y2 - x2 * y1)
    return abs(total_area) // 2

def shifted_table(pos):
    table = [((-1, 0), "|7F"), ((1, 0), "|LJ"), ((0, -1), "-LF"), ((0, 1), "-J7")]

    y, x = pos
    return [((y + dy, x + dx), pipes) for (dy, dx), pipes in table]

def get_start(start, lines):
    return [(y, x) for (y, x), pipes in shifted_table(start) if lines[y][x] in pipes][0]

def get_direction(start, lines, visited):
    y, x = start
    el = lines[y][x]

    # Труба, левая координата, правая координата, прошлая координата, следующая координата
    table = {"F": ([(0, 0)], [(1, 1)], (1, 0), (0, 1)),
             "L": ([(1, 0)], [(0, 1)], (0, 1), (-1, 0)),
             "J": ([(0, 0)], [(1, 1)], (0, -1), (-1, 0)),
             "7": ([(1, 0)], [(0, 1)], (1, 0), (0, -1)),
             "|": ([(0, 0), (1, 0)], [(0, 1), (1, 1)], (1, 0), (-1, 0)),
             "-": ([(0, 0), (0, 1)], [(1, 0), (1, 1)], (0, -1), (0, 1))
            }

    cor_l_dir, cor_r_dir, first_dir, second_dir = table[el]

    cords_l = [shifted(dir, y, x) for dir in cor_l_dir]
    cords_r = [shifted(dir, y, x) for dir in cor_r_dir]
    first_cor = shifted(first_dir, y, x)
    second_cor = shifted(second_dir, y, x)

    if first_cor not in visited:
        return first_cor, cords_l, cords_r
    elif second_cor not in visited:
        return second_cor, cords_r, cords_l

def shifted(dir, y, x):
    shift_y, shift_x = dir
    return shift_y + y, shift_x + x

def print_map(lines, start):
    for y, line in enumerate(lines):
        for x, el in enumerate(line):
            if (y, x) == start:
                print("*", end="")
            else:
                print(el, end="")

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-10/input.txt"
    main(file_name)



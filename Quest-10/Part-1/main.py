import sys

def main(file_name):
    lines = read_file(file_name)
    start = find_start(lines)
    route = find_route(lines, start)
    print(route)

def read_file(name):
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.readlines()

def find_start(lines):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == 'S':
                return (y, x)

def find_route(lines, start):
    """
    >>> find_route(['..F7.\n', '.FJ|.\n', 'SJ.L7\n', '|F--J\n', 'LJ...\n'], (0, 2))
    """
    visited = set()
    visited.add(start)
    starts = get_starts(start, lines)

    while starts[0] != starts[1]:
        visited.add(starts[0])
        visited.add(starts[1])
        starts = [get_direction(pos, lines, visited) for pos in starts]

    return (len(visited) + 1) // 2

def shifted_table(pos):
    table = [((-1, 0), "|7F"), ((1, 0), "|LJ"), ((0, -1), "-LF"), ((0, 1), "-J7")]

    y, x = pos
    return [((y + dy, x + dx), pipes) for (dy, dx), pipes in table]

def shifted_y_x(pos):
    table = [((1, 0), "|7F"), ((-1, 0), "|LJ"), ((0, 1), "-LF"), ((0, -1), "-J7")]

    y, x = pos
    return [((y + dy, x + dx), pipes) for (dy, dx), pipes in table]

def get_starts(start, lines):
    return [(y, x) for (y, x), pipes in shifted_table(start) if lines[y][x] in pipes]

def get_direction(start, lines, visited):
    y, x = start
    el = lines[y][x]
    for pos, pipes in shifted_y_x(start):
        if el in pipes and pos not in visited:
            return pos

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-10/input.txt"
    main(file_name)

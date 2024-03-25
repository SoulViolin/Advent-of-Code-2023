import sys

def main(file_name):
    lines = read_file(file_name)
    start = find_start(lines)
    route = find_route(lines, start)

def read_file(name):
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.readlines()

def find_start(lines):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == 'S':  # Начальная точка
                return (x, y)

def find_route(lines, start):
    """
    >>> find_route(['..F7.\n', '.FJ|.\n', 'SJ.L7\n', '|F--J\n', 'LJ...\n'], (0, 2))
    """
    visited = set()
    route = []
    current_x, current_y = start

    while ((current_x, current_y) != start and len(route) < 2) is False:
        directions = get_directions(current_y, current_x, lines)
        for dir in directions:
            checked_y = current_y + dir[0]
            checked_x = current_x + dir[1]
            if 0 <= checked_y < len(lines) and 0 <= checked_x < len(lines[y]):
                el = lines[checked_y][checked_x]
                # Up
                if dir == (-1, 0):
                    print(f"Up: {el}", checked_y, checked_x, dir)
                    if el in "|7F" and (checked_y, checked_x) not in visited:
                        visited.add((checked_y, checked_x))
                        print("True")
                # Down
                if dir == (1, 0):
                    print(f"Down: {el}", checked_y, checked_x, dir)
                    if el in "|LJ" and (checked_y, checked_x) not in visited:
                        visited.add((checked_y, checked_x))
                        print("True")
                # Left
                if dir == (0, -1):
                    print(f"Left: {el}", checked_y, checked_x, dir)
                    if el in "-LF" and (checked_y, checked_x) not in visited:
                        visited.add((checked_y, checked_x))
                        print("True")
                # Right
                if dir == (0, 1):
                    print(f"Right: {el}", checked_y, checked_x, dir)
                    if el in "-J7" and (checked_y, checked_x) not in visited:
                        visited.add((checked_y, checked_x))
                        print("True")

                print(visited)
                input()

def get_directions(y, x, lines):
    directions = []
    if lines[y][x] == "S":
        return [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # if x > 0 and lines[y][x-1] in '-J7':  # Движение вверх
    #     directions.append((-1, 0))
    # if x < len(lines[y]) - 1 and lines[y][x+1] in '-LF':  # Движение вниз
    #     directions.append((1, 0))
    # if y > 0 and lines[y-1][x] in '|LJ':  # Движение влево
    #     directions.append((0, -1))
    # if y < len(lines) - 1 and lines[y+1][x] in '|7F':  # Движение вправо
    #     directions.append((0, 1))
    # return directions

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-10/test.txt"
    main(file_name)



# # Функция для определения возможных направлений из текущей позиции
# def possible_directions(x, y, lines):
#     directions = []
#     if x > 0 and route_array[y][x-1] in '-J7':  # Движение вверх
#         directions.append((-1, 0))
#     if x < len(route_array[y]) - 1 and route_array[y][x+1] in '-LF':  # Движение вниз
#         directions.append((1, 0))
#     if y > 0 and route_array[y-1][x] in '|LJ':  # Движение влево
#         directions.append((0, -1))
#     if y < len(route_array) - 1 and route_array[y+1][x] in '|7F':  # Движение вправо
#         directions.append((0, 1))
#     return directions


import sys

def main(file_name: str) -> None:
    lines = read_file(file_name)
    grid = gravity_simulation(lines)
    result = calculate_total_load(grid)
    print(result)

def read_file(name: str) -> list[str]:
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.read().splitlines()

def gravity_simulation(grid):
    rows = len(grid)
    cols = len(grid[0])

    for col in range(cols):
        for row in range(rows):
            if grid[row][col] == 'O':
                current_row = row
                while can_move_up(current_row, col, grid):
                    if grid[current_row - 1][col] == '.':
                        grid[current_row] = grid[current_row][:col] + '.' + grid[current_row][col + 1:]
                        grid[current_row - 1] = grid[current_row - 1][:col] + 'O' + grid[current_row - 1][col + 1:]
                        current_row -= 1
                    else:
                        break

    return grid

def can_move_up(x, y, grid):
    return x - 1 >= 0 and (grid[x - 1][y] == '.' or grid[x - 1][y] == 'O')

def calculate_total_load(platform):
    total_load = 0
    rows = len(platform)

    for row_index in range(rows - 1, -1, -1):
        row = platform[row_index]

        for col_index in range(len(row)):
            if row[col_index] == 'O':
                load = rows - row_index
                total_load += load

    return total_load

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-14/input.txt"
    main(file_name)

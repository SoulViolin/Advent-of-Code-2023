import sys

def main(file_name: str) -> None:
    lines = read_file(file_name)
    platforms = [gravity_simulation(grid) for grid in lines]
    result = sum([calculate_total_load(platform) for platform in platforms])
    print("Суммарный total load для камней 'O':", result)

def read_file(name: str) -> list[list[str]]:
    with open(file=name, mode="r", encoding="utf-8") as f:
        return [el.splitlines() for el in f.read().split("\n\n")]

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
    rows = platform.strip().split('\n')[::-1]
    total_load = 0

    for row_idx, row in enumerate(rows):
        for char in row:
            if char == 'O':
                load = row_idx + 1
                total_load += load

    return total_load

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "test-1.txt"
    main(file_name)

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

grid = [
    "O....#....",
    "O.OO#....#",
    ".....##...",
    "OO.#O....O",
    ".O.....O#.",
    "O.#..O.#.#",
    "..O..#O..O",
    ".......O..",
    "#....###..",
    "#OO..#...."
]

new_grid = gravity_simulation(grid)

for row in new_grid:
    print(row)


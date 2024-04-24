# def gravity_simulation(grid):
#     rows = len(grid)
#     cols = len(grid[0])

#     for _ in range(4):
#         for col in range(cols):
#             for row in range(1, rows):
#                 if grid[row][col] == 'O':
#                     current_row = row
#                     while current_row > 0 and grid[current_row - 1][col] == '.':
#                         grid[current_row] = grid[current_row][:col] + '.' + grid[current_row][col + 1:]
#                         grid[current_row - 1] = grid[current_row - 1][:col] + 'O' + grid[current_row - 1][col + 1:]
#                         current_row -= 1

#         for row in range(rows):
#             for col in range(1, cols):
#                 if grid[row][col] == 'O':
#                     current_col = col
#                     while current_col > 0 and grid[row][current_col - 1] == '.':
#                         grid[row] = grid[row][:current_col] + '.' + grid[row][current_col + 1:]
#                         grid[row] = grid[row][:current_col - 1] + 'O' + grid[row][current_col:]
#                         current_col -= 1

#         for col in range(cols):
#             for row in range(rows - 2, -1, -1):
#                 if grid[row][col] == 'O':
#                     current_row = row
#                     while current_row < rows - 1 and grid[current_row + 1][col] == '.':
#                         grid[current_row] = grid[current_row][:col] + '.' + grid[current_row][col + 1:]
#                         grid[current_row + 1] = grid[current_row + 1][:col] + 'O' + grid[current_row + 1][col + 1:]
#                         current_row += 1

#         for row in range(rows):
#             for col in range(cols - 2, -1, -1):
#                 if grid[row][col] == 'O':
#                     current_col = col
#                     while current_col < cols - 1 and grid[row][current_col + 1] == '.':
#                         grid[row] = grid[row][:current_col] + '.' + grid[row][current_col + 1:]
#                         grid[row] = grid[row][:current_col + 1] + 'O' + grid[row][current_col + 2:]
#                         current_col += 1
#     return grid

def gravity_simulation(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    # Преобразуем grid в список списков (список строк)
    grid = [list(row) for row in grid]
    
    for _ in range(1000000000):
        # Создадим временный массив для хранения результатов обработки
        new_grid = [row[:] for row in grid]
        
        # Север
        for col in range(cols):
            last_row = rows - 1
            for row in range(rows - 1, -1, -1):
                if grid[row][col] == 'O':
                    new_grid[last_row][col] = 'O'
                    last_row -= 1
            # Записываем точки
        # Запад
        for row in range(rows):
            write_index = 0
            for col in range(cols):
                if new_grid[row][col] == 'O':
                    new_grid[row][write_index] = 'O'
                    write_index += 1
            for col in range(write_index, cols):
                new_grid[row][col] = '.'
        # Юг
        for col in range(cols):
            first_row = 0
            for row in range(rows):
                if new_grid[row][col] == 'O':
                    new_grid[first_row][col] = 'O'
                    first_row += 1
            # Доставляем точки
        # Восток
        for row in range(rows):
            write_index = cols - 1
            for col in range(cols - 1, -1, -1):
                if new_grid[row][col] == 'O':
                    new_grid[row][write_index] = 'O'
                    write_index -= 1
            for col in range(write_index, -1, -1):
                new_grid[row][col] = '.'

        # Обновляем grid для следующей итерации
        grid = new_grid
    
    # Преобразуем обратно в список строк для возврата результата
    grid = [''.join(row) for row in grid]
    return grid

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


# for row in grid:
#     print(row)

# print("\n-----------------------------------\n")





# def count_reflections(pattern):
#     return find_horizontal_reflection(flip(pattern)) + 100 * find_horizontal_reflection(pattern)

# def find_horizontal_reflection(pattern):
#     for i in range(1, len(pattern)):
#         if does_reflect(pattern, i):
#             return i
#     return 0

# def does_reflect(pattern, point):
#     mirror_indexes = get_mirror_indexes(len(pattern), point)
#     return all(pattern[x] == pattern[y] for x, y in mirror_indexes)

# def get_mirror_indexes(length, point):
#     max_delta = min(point, length - point)
#     return [(point - delta - 1, point + delta) for delta in range(max_delta)]






# def flip(pattern):
#     return [row[::-1] for row in pattern]

# def flip_matrix(matrix):
#     if not matrix:
#         return []

#     num_rows = len(matrix)
#     num_cols = len(matrix[0])

#     flipped_matrix = []
#     for col in range(num_cols):
#         new_row = ''.join(matrix[row][col] for row in range(num_rows))
#         flipped_matrix.append(new_row)

#     return flipped_matrix

def flip_matrix(matrix):
    return [''.join(row[col] for row in matrix) for col in range(len(matrix[0]))]

def find_horizontal_reflection(pattern):
    n = len(pattern)
    for i in range(1, n):
        if all(pattern[i - j - 1] == pattern[i + j] for j in range(min(i, n - i))):
            return i
    return 0

# Примеры использования функций:

print(find_horizontal_reflection(["aaa", "aaa", "bbb"]))  #=> 1
print(find_horizontal_reflection(["aaa", "bbb", "ccc", "ccc", "bbb"]))  #=> 3
print(find_horizontal_reflection(["aaa", "bbb", "ccc"]))  #=> 0

print(flip_matrix(["aaa", "bbb", "ccc"]))

print(find_horizontal_reflection(["#...##..#", "#....#..#", "..##..###", "#####.##.", "#####.##.", "..##..###", "#....#..#"]))



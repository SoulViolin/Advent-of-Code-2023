import sys

def main(file_name: str) -> None:
    lines = read_file(file_name)

    print(sum([calculate(matrix) for matrix in lines]))

def read_file(name: str) -> list[list[str]]:
    with open(file=name, mode="r", encoding="utf-8") as f:
        return [el.splitlines() for el in f.read().split("\n\n")]

def calculate(lines: list[str]) -> int:
    horizontal = find_mirror(lines) * 100
    vertical = find_mirror(flip_matrix(lines))

    mirror = horizontal + vertical

    return mirror

def find_mirror(lines: list[str]) -> int:
    """
    >>> horizontal_mirror([
    ... "#...##..#",    # 0
    ... "#....#..#",    # 1
    ... "..##..###",    # 2
    ... "#####.##.",    # 3
    ... "#####.##.",    # 4
    ... "..##..###",    # 5
    ... "#....#..#"     # 6
    ... ])
    4
    """
    n = len(lines)
    for i in range(1, n):
        if all(lines[i - j - 1] == lines[i + j] for j in range(min(i, n - i))):
            return i
    return 0

        # 1 "#...##..#" 2 "#....#..#" if row1 == row2: mirror!!! == index (1) else: row1 + row2 == row3 + row4
        # 0 == 1                                                return 1
        # 0 == 3 and 1 == 2                                     return 2
        # 0 == 5 and 1 == 4 and 2 == 3                          return 3
        # (0 == 7) 1 == 6 and 2 == 5 and 3 == 4                 return 4
        # (0 == 9, 1 == 8, 2 == 7) 3 == 6 and 4 == 5            return 5
        # (0 == 11, 1 == 10, 2 == 9, 3 == 8, 4 == 7) 5 == 6     return 6

        # 0 == 1                                                return 1
        # 0 == 3 and 1 == 2                                     return 2
        # 0 == 5 and 1 == 4 and 2 == 3                          return 3
        # 1 == 6 and 2 == 5 and 3 == 4                          return 4
        # 3 == 6 and 4 == 5                                     return 5
        # 5 == 6                                                return 6

        # 3 == 4 and 2 == 5 and 1 == 6 return 4

def flip_matrix(matrix: list[str]) -> list[str]:
    return [''.join(row[col] for row in matrix) for col in range(len(matrix[0]))]

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-13/input.txt"
    main(file_name)






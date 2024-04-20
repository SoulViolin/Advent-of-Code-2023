import sys
from thefuzz import fuzz

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
    n = len(lines)
    for i in range(1, n):
        # if sum([diff_count(lines[i - j - 1], lines[i + j]) for j in range(min(i, n - i))]) <= 1:
        #     return i
        diff = 0
        for j in range(min(i, n - i)):
            diff += diff_count(lines[i - j - 1], lines[i + j])

            if diff > 1:
                break

        if diff == 1:
            return i
    return 0

def diff_count(word1, word2) -> int:
    if word1 == word2:
        return 0

    # Считаем количество несовпадающих символов
    diff_count = sum(1 for c1, c2 in zip(word1, word2) if c1 != c2)

    return diff_count

def flip_matrix(matrix: list[str]) -> list[str]:
    return [''.join(row[col] for row in matrix) for col in range(len(matrix[0]))]

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-13/input.txt"
    main(file_name)

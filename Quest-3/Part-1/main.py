def main(fileName):
    lines = readFile(fileName)

    schemEngine = [list(line.rstrip("\n")) for line in lines]
    symbols = set(char for line in schemEngine for char in line if char != '.' and not char.isdigit())

    allNumbers = findNumbers(schemEngine)
    trueNumbers = findSymbolsAroundNumbers(schemEngine, allNumbers, symbols)

    total = sum(trueNumbers)
    print(total)

def readFile(name):
    with open(file=f"Quest-3/{name}", mode="r", encoding="utf-8") as f:
        return f.readlines()

def findNumbers(matrix):
    """
    Function to find numbers in matrix
    :param matrix: list of lists
    :return: list of numbers and their coordinates

    >>> findNumbers([["1", "2", "3"], ["4", ".", "6"], ["7", ".", "."]])
    [[123, [[0, 0], [0, 1], [0, 2]]], [4, [[1, 0]]], [6, [[1, 2]]], [7, [[2, 0]]]]

    """
    numbers = []
    visited = set()
    rows = len(matrix)
    cols = len(matrix[0])

    def explore(row, col):
        num = []
        # Explore horizontally
        for c in range(col, cols):
            if matrix[row][c].isdigit() and (row, c) not in visited:
                num.append({"digit": matrix[row][c], "coordinates": [row, c]})
                visited.add((row, c))
            else:
                break

        if num != []:
            return num
        else:
            return None

    for row in range(rows):
        for col in range(cols):
            num = explore(row, col)
            if num:
                digit = [el["digit"] for el in num]
                coordinates = [el["coordinates"] for el in num]

                numbers.append([int("".join(digit)), coordinates])

    return numbers

def findSymbolsAroundNumbers(matrix, numbers, symbols):
    results = []

    for numberKey, coordinates in numbers:
        symbolCoordinates = None
        for coord in coordinates:
            row, col = coord
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                newRow, newCol = row + dr, col + dc
                if (0 <= newRow < len(matrix) and 0 <= newCol < len(matrix[0]) and matrix[newRow][newCol] in symbols and (newRow, newCol) not in coordinates):
                    symbolCoordinates = (newRow, newCol)
                    break

            if symbolCoordinates:
                break

        if symbolCoordinates:
            results.append(int(numberKey))

    return results


if __name__ == '__main__':
    fileName = "input.txt"
    main(fileName)

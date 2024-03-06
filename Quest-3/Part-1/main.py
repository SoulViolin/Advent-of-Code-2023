def main(fileName):
    lines = readFile(fileName)

    schemEngine = [list(line.replace("\n", "")) for line in lines]
    symbols = set(char for line in schemEngine for char in line if char != '.' and not char.isdigit())

    allNumbers = findNumbers(schemEngine, symbols)
    trueNumbers = findSymbolsAroundNumbers(schemEngine, allNumbers, symbols)

    total = sum(trueNumbers)
    print(total)

def readFile(name):
    with open(file=f"Quest-3/{name}", mode="r", encoding="utf-8") as f:
        return f.readlines()

def findNumbers(matrix, symbols):
    visited = set()
    numbers = {}

    def exploreNumber(row, col):
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or (row, col) in visited or matrix[row][col] == '.' or matrix[row][col] in symbols:
            return []

        visited.add((row, col))
        number = [(row, col)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in directions:
            newRow, newCol = row + dr, col + dc
            number += exploreNumber(newRow, newCol)

        return number

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j].isdigit() and (i, j) not in visited:
                numberCoordinates = exploreNumber(i, j)
                numKey = ''.join(matrix[i][j] for i, j in numberCoordinates)
                numbers[numKey] = numberCoordinates

    return numbers

def findSymbolsAroundNumbers(matrix, numbers, symbols):
    results = []

    for numberKey, coordinates in numbers.items():
        foundSymbol = False
        for coord in coordinates:
            row, col = coord
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                newRow, newCol = row + dr, col + dc
                if (newRow, newCol) in coordinates:
                    continue  # Skip a cell if it is part of the same number
                if 0 <= newRow < len(matrix) and 0 <= newCol < len(matrix[0]) and matrix[newRow][newCol] in symbols:
                    foundSymbol = True
                    break
            if foundSymbol:
                break

        if foundSymbol:
            results.append(int(numberKey))

    return results


if __name__ == '__main__':
    fileName = "input.txt"
    main(fileName)
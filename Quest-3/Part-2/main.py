from pprint import pprint

def main(fileName):
    lines = readFile(fileName)

    schemEngine = [list(line.rstrip("\n")) for line in lines]
    symbols = set("*")

    allNumbers = findNumbers(schemEngine)
    trueNumbers = findSymbolsAroundNumbers(schemEngine, allNumbers, symbols)
    gearRatios = findGearRatios(trueNumbers)

    total = sum(trueNumbers)
    print(total)

def readFile(name):
    with open(file=f"Quest-3/{name}", mode="r", encoding="utf-8") as f:
        return f.readlines()

def findNumbers(matrix):
    numbers = []
    visited = set()
    rows = len(matrix)
    cols = len(matrix[0])

    def explore(row, col):
        num = []
        num.append({"digit": matrix[row][col], "coordinates": [row, col]})
        # Explore horizontally
        for c in range(col + 1, cols):
            if matrix[row][c].isdigit() and (row, c) not in visited:
                num.append({"digit": matrix[row][c], "coordinates": [row, c]})
                visited.add((row, c))
            else:
                break
        # Explore vertically
        for r in range(row + 1, rows):
            if matrix[r][col].isdigit() and (r, col) not in visited:
                num.append({"digit": matrix[r][col], "coordinates": [r, col]})
                visited.add((r, col))
            else:
                break
        return num

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col].isdigit() and (row, col) not in visited:
                num = explore(row, col)
                digit = [el["digit"] for el in num]
                coordinates = [el["coordinates"] for el in num]

                numbers.append([int("".join(digit)), coordinates])

    return numbers

def findSymbolsAroundNumbers(matrix, numbers, symbols):
    results = []

    for numberKey, coordinates in numbers:
        symbol_coordinates = ()
        foundSymbol = False
        for coord in coordinates:
            row, col = coord
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                newRow, newCol = row + dr, col + dc
                if (newRow, newCol) in coordinates:
                    continue  # Skip a cell if it is part of the same number
                if 0 <= newRow < len(matrix) and 0 <= newCol < len(matrix[0]) and matrix[newRow][newCol] in symbols:
                    foundSymbol = True
                    symbol_coordinates = (newRow, newCol)
                    break
            if foundSymbol:
                break

        if foundSymbol:
            results.append((int(numberKey), symbol_coordinates))

    return results

findGearRatios():


if __name__ == '__main__':
    fileName = "input.txt"
    main(fileName)

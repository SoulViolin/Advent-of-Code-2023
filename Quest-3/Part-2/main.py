def main(fileName):
    lines = readFile(fileName)
    symbols = ["*"]

    allNumbers, allSymbols = findNumbersSymbols(lines, symbols)
    trueNumbers = findSymbolsAroundNumbers(allNumbers, allSymbols)
    gearRatios = findGearRatios(trueNumbers)

    total = sum(gearRatios)
    print(total)

def readFile(name):
    with open(file=f"Quest-3/{name}", mode="r", encoding="utf-8") as f:
        return f.readlines()

def findNumbersSymbols(lines, symbols):
    numbers = []
    allSymbols = []
    for i, line in enumerate(lines):
        number = ""
        coordinates = []
        for j, char in enumerate(line):
            if char.isdigit():
                number += char
                coordinates.append([i, j])
            elif number:
                numbers.append({"digit": int(number), "coordinates": coordinates})
                number = ""
                coordinates = []
            elif char in symbols:
                allSymbols.append([i, j])
        if number:
            numbers.append({"digit": int(number), "coordinates": coordinates})
    return numbers, allSymbols

def findSymbolsAroundNumbers(numbers, symbols):
    trueNumbers = []
    for number in numbers:
        for i, j in number["coordinates"]:
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
            for dx, dy in directions:
                if [i + dx, j + dy] in symbols and [number["digit"], (i + dx, j + dy)] not in trueNumbers:
                    trueNumbers.append([number["digit"], (i + dx, j + dy)])
                    break

    return trueNumbers

def findGearRatios(data):
    result = []
    coordinates = {}

    # Creating a dictionary where the keys will be coordinates and the values will be an array of values
    for value, coords in data:
        if coords in coordinates:
            coordinates[coords].append(value)
        else:
            coordinates[coords] = [value]

    # Iterate over the coordinates and multiply the elements of the array, if there are more than one
    for coords, values in coordinates.items():
        if len(values) > 1:
            product = 1
            for val in values:
                product *= val
            result.append(product)

    return result

if __name__ == '__main__':
    fileName = "input.txt"
    main(fileName)

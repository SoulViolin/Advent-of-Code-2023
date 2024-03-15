import sys
import math

def main(lines):
    # """
    # >>> main(["1*1", "111", "111"])
    # ['1', '1', '1', '1', 1]

    # >>> main([".*1", "...", "..."])
    # ['1']
    # """
    numbersAll = [findNumbers(line) for line in lines]

    gearRatio = []
    for y, line in enumerate(lines):
        for x, el in enumerate(line):
            if el == "*":
                numbers = []

                if y-1 >= 0:
                    numbers += numbersAll[y-1]

                numbers += numbersAll[y]

                if y+1 < len(lines):
                    numbers += numbersAll[y+1]

                touchedNumbers = filterNumbers(numbers, x)

                if len(touchedNumbers) == 2:
                    ratio = int(touchedNumbers[0]) * int(touchedNumbers[1])
                    gearRatio.append(ratio)

    total = sum(gearRatio)
    return total

def findNumbers(line):
    # """
    # >>> findNumbers("231*.1")
    # [('231', 0)]

    # >>> findNumbers("1*.")
    # [('1', 0)]

    # >>> findNumbers(".*.")
    # []
    # """

    allNumbers = []
    number = ""

    for dx, el in enumerate(line):
        if el.isdigit():
            number += el
        elif number:
            allNumbers.append((number, dx - len(number)))
            number = ""
    if number:
        allNumbers.append((number, dx - len(number)))

    return allNumbers

def filterNumbers(numbers, x):
    # """
    # >>> filterNumbers([("231", 0), ("43", 3)], 1)
    # ['231']

    # >>> filterNumbers([("231", 0), ("43", 3)], 2)
    # ['231', '43']
    # """
    touchedNumbers = []

    for number, dx in numbers:
        if overlap(dx, dx + len(number) - 1, x - 1, x + 1):
            touchedNumbers.append(int(number))

    return touchedNumbers

def overlap(a, b, c, d):
    """
    >>> overlap(0, 4, 4, 6)
    True

    >>> overlap(0, 4, 0, 4)
    True

    >>> overlap(0, 4, 5, 7)
    False
    """
#     0123456
#         c*d
#     a===b
    return a <= c <= b or c <= a <= d

def readFile(name):
    with open(name, mode="r", encoding="utf-8") as f:
        return f.readlines()

if __name__ == '__main__':
    try:
        fileName = sys.argv[1]
    except:
        fileName = "Quest-3/input.txt"
    lines = readFile(fileName)
    print(main(lines))


import re

def main():
    calibrationValues = []

    fileName = "input.txt"
    file = readFile(fileName)

    for el in file:
        numbers = re.findall(r'\d', el)
        calibration = int(str(numbers[0]) + numbers[-1])
        calibrationValues.append(calibration)

    total = sum(calibrationValues)
    print(total)

def readFile(name):
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.readlines()

if __name__ == '__main__':
    main()

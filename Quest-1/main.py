import re

def main():
    calibrationValues = []
    word_to_number = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    fileName = "input.txt"
    file = readFile(fileName)

    for el in file:
        numbers = re.findall(r'(?:zero|one|two|three|four|five|six|seven|eight|nine|\d)', el)
        numbers = ''.join(numbers)
        for word, number in word_to_number.items():
            numbers = numbers.replace(word, number)

        numbers = re.findall(r'\d', numbers)
        calibration = int(str(numbers[0]) + numbers[-1])
        calibrationValues.append(calibration)

    total = sum(calibrationValues)
    print(total)

def readFile(name):
    with open(file=f"Quest-1/{name}", mode="r", encoding="utf-8") as f:
        return f.readlines()

if __name__ == '__main__':
    main()

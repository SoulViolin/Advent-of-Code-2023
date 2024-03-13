import re

def main():
    fileName = "input.txt"
    lines = readFile(fileName)

    listWinCount = []

    for line in lines:
        card = line.rstrip("\n").split(': ')[1]
        winNumbers = re.findall(r'\d+', card.split(" | ")[0])
        cardNumbers = re.findall(r'\d+', card.split(" | ")[1])

        win = calculateWin(winNumbers, cardNumbers)
        listWinCount.append(win)

    totalWin = sum(listWinCount)
    print(totalWin)

def calculateWin(winNumbers, cardNumbers):
    winCount = 0

    for number in cardNumbers:
        if number in winNumbers:
            if winCount == 0:
                winCount += 1
            else:
                winCount *= 2

    return winCount

def readFile(name):
    with open(file=f"Quest-4/{name}", mode="r", encoding="utf-8") as f:
        return f.readlines()

if __name__ == '__main__':
    main()

import re

def main():
    fileName = "input.txt"
    lines = readFile(fileName)

    cards = getcards(lines)

    for card in cards:
        win = calculateWin(card["winNumbers"], card["cardNumbers"])
        if win != 0:
            for i in range(card["cardNumber"], card["cardNumber"] + win):
                cards.append(cards[i])

    totalWin = len(cards)
    print(totalWin)

def getcards(lines):
    cards = []

    for line in lines:
        card = line.rstrip("\n").split(': ')[1]
        cardNumber = int(re.findall(r'\d+', line.rstrip("\n").split(': ')[0])[0])
        winNumbers = re.findall(r'\d+', card.split(" | ")[0])
        cardNumbers = re.findall(r'\d+', card.split(" | ")[1])

        cards.append({"cardNumber": cardNumber, "winNumbers": winNumbers, "cardNumbers": cardNumbers})
    return cards

def calculateWin(winNumbers, cardNumbers):
    winCount = 0

    for number in cardNumbers:
        if number in winNumbers:
            winCount += 1
    return winCount

def readFile(name):
    with open(file=f"Quest-4/{name}", mode="r", encoding="utf-8") as f:
        return f.readlines()

if __name__ == '__main__':
    main()
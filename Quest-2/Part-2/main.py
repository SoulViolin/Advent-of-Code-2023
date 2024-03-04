def main():
    appropriateValue = []

    fileName = "input.txt"
    lines = readFile(fileName)

    for el in lines:
        name, count = el.split(": ")[0].split(" ")
        games = [{item.split()[1]: int(item.split()[0]) for item in game.split(", ")} for game in el.split(": ")[1].split("; ")]

        MGred = max([game.get("red", 0) for game in games] + [1])
        MGgreen = max([game.get("green", 0) for game in games] + [1])
        MGblue = max([game.get("blue", 0) for game in games] + [1])
        
        total = MGred * MGgreen * MGblue
        appropriateValue.append(total)
    
    total = sum(appropriateValue)
    print(total)

def readFile(name):
    with open(file=f"Quest-2/{name}", mode="r", encoding="utf-8") as f:
        return f.readlines()

if __name__ == '__main__':
    main()
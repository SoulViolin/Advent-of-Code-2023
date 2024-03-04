def main(Mred, Mgreen, Mblue):
    appropriateValue = []

    fileName = "input.txt"
    file = readFile(fileName)

    for el in file:
        flag = True

        name, count = el.split(": ")[0].split(" ")
        games = [{item.split()[1]: int(item.split()[0]) for item in game.split(", ")} for game in el.split(": ")[1].split("; ")]

        MGred = 1
        MGgreen = 1
        MGblue = 1

        for game in games:
            Gred = game.get("red", 0)
            Ggreen = game.get("green", 0)
            Gblue = game.get("blue", 0)

            MGred = max(MGred, Gred)
            MGgreen = max(MGgreen, Ggreen)
            MGblue = max(MGblue, Gblue)

            if Gred <= Mred and Ggreen <= Mgreen and Gblue <= Mblue:
                pass
            else:
                # flag = False
                pass
        
        if flag: 
            total = MGred * MGgreen * MGblue
            appropriateValue.append(total)
    
    total = sum(appropriateValue)
    print(total)

def readFile(name):
    with open(file=f"Quest-2/{name}", mode="r", encoding="utf-8") as f:
        return f.readlines()

if __name__ == '__main__':
    try:
        red, green, blue = input("Maximum number of cubes: Red, Green, Blue\n").split(", ")
    except:
        red, green, blue = 12, 13, 14

    print(f"Maximum number of cubes: Red-{red}, Green-{green}, Blue-{blue}")
    main(red, green, blue)
import sys
from pprint import pprint

def main(fileName):
    lines = readFile(fileName)
    data = getData(lines)
    processedData = processData(data)
    print(processedData)

    # unificationData = unificationData(processedData)

    # pprint(data)

def getData(lines):
    data = {}
    values = []

    for line in lines:
        if "seeds" in line:
            key, value = line.split(": ")
            values += [int(el) for el in value.rstrip("\n").split()]
            data[key] = values
        else:
            if ":" in line:
                key = line.rsplit(":\n")[0]
                values = []
            elif "\n" != line:
                values.append([int(el) for el in line.rstrip("\n").split()])
            else:
                data[key] = values

    return data

def processData(data):
    newData = {}

    for key, value in data.items():
        if key == "seeds":
            newData[key] = value
        else:
            processedData = handler(value)
            newData[key] = processedData

    return newData

def handler(value):
    """
    >>> handler([[50, 98, 2], [50, 98, 2]])
    [[98, 50], [99, 51], [98, 50], [99, 51]]
    """
    values = []

    for el in value:
        fields = [i for i in range(el[0], el[0] + el[2])]
        seeds = [i for i in range(el[1], el[1] + el[2])]
        values += [list(g) for g in zip(seeds, fields)]

    return values

# def unificationData(data):
#     newData = {}

#     for key, value in data.items():
#         if key == "seeds":
#             newData[key] = value
#         else:
#             # value = joiningData(value)
#             pass

#     return newData

# def joiningData(value):

def readFile(name):
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.readlines()

if __name__ == '__main__':
    try:
        fileName = sys.argv[1]
    except:
        fileName = "Quest-5/input.txt"
    main(fileName)

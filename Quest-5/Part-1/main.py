from pprint import pprint

def main(fileName):
    lines = readFile(fileName)
    getValues(lines)

def getValues(lines):
    key_value_pairs = {}
    key = None
    value = ''
    for line in lines:
        line = line.strip()
        if not line:
            if key is not None:
                key_value_pairs[key] = value.strip()
                key = None
                value = ''
        elif ':' in line:
            parts = line.split(':', 1)
            if key is not None:
                key_value_pairs[key] = value.strip()
            key = parts[0].strip()
            value += parts[1].strip() + ' '
        elif key is not None:
            value += line + ' '
    if key is not None:
        key_value_pairs[key] = value.strip()

    pprint(key_value_pairs)


def readFile(name):
    with open(file=f"Quest-5/{name}", mode="r", encoding="utf-8") as f:
        return f.readlines()

if __name__ == '__main__':
    fileName = "input.txt"
    main(fileName)

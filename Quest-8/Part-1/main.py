import sys

def main(file_name):
    lines = read_file(file_name)
    instructions = [el for el in lines[0].rstrip()]
    nodes = {line.split('=')[0].strip(): tuple(line.split('=')[1][2:-2].split(', ')) for line in sorted(lines[2:])}

    len = route_length(instructions, nodes)
    print(len)

def read_file(name):
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.readlines()

def route_length(instructions, nodes):
    current_node = 'AAA'

    route_length = 0

    while current_node != 'ZZZ':
        for instruction in instructions:
            if instruction == "L":
                current_node = nodes[current_node][0]
            else:
                current_node = nodes[current_node][1]
            route_length += 1

    return route_length

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-8/input.txt"
    main(file_name)

import sys
import math
from functools import reduce

def main(file_name):
    lines = read_file(file_name)
    instructions = [el for el in lines[0].rstrip()]
    nodes = {line.split('=')[0].strip(): tuple(line.split('=')[1][2:-2].split(', ')) for line in sorted(lines[2:])}

    route_len = route_length(instructions, nodes)
    print(route_len)

def read_file(name):
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.readlines()

def route_length(instructions, nodes):
    current_nodes = [node for node in nodes if node.endswith("A")]

    cycles  = []

    for current_node in current_nodes:
        cycles.append(count_moves(nodes, current_node, instructions))

    return reduce(lcm, cycles)

def count_moves(nodes, starting_point, moves):
    count = 0
    current = starting_point

    while current[-1] != "Z":
        current_move = 0 if moves[count % len(moves)] == "L" else 1
        current = nodes[current][current_move]
        count += 1

    return count

def lcm(a, b):
    return a * b // math.gcd(a, b)

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-8/input.txt"
    main(file_name)

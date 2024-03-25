import sys

def main(file_name):
    lines = read_file(file_name)
    sequences = [[int(el) for el in line.rstrip().split()] for line in lines]
    print(sum([extrapolation(sequence) for sequence in sequences]))

def read_file(name):
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.readlines()

def extrapolation(sequence):
    if all(x == 0 for x in sequence):
        return 0
    next_sequence = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
    return sequence[0] - extrapolation(next_sequence)

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-9/input.txt"
    main(file_name)

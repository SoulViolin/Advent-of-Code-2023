import sys

def main(file_name):
    lines = read_file(file_name)
    histories = [calculate_history([int(el) for el in line.rstrip().split()]) for line in lines]
    last_el_histories = [[sublist[-1] for sublist in history] for history in histories]
    print(sum([sum([el for el in history]) for history in last_el_histories]))

def read_file(name):
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.readlines()

def calculate_history(sequence):
    """
    >>> calculate_history([0, 3, 6, 9, 12, 15])
    [[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0, 0, 0, 0]]
    """
    history = [sequence]
    while len(sequence) > 1 and not all(x == 0 for x in sequence):
        sequence = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
        history.append(sequence)
    return history

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-9/input.txt"
    main(file_name)

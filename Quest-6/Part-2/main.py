import sys
import math
from functools import reduce

def main(file_name):
    input = read_file(file_name)
    times, records = get_data(input)
    wins = wins_count(times, records)

    print(wins)

def read_file(name):
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.readlines()

def get_data(input):
    times = [int(''.join([time for time in input[0].rstrip("\n").split(":")[1].split()]))]
    records = [int(''.join([record for record in input[1].rstrip("\n").split(":")[1].split()]))]

    return times, records

def wins_count(times, records):
    items = [win_count(time, record) for time, record in zip(times, records)]
    total_win = reduce((lambda x, y: x * y), items)

    return total_win

def win_count(time, record):
    """
    >>> win_count(7, 9)
    (2, 5, 4)
    >>> win_count(15, 40)
    (4, 11, 8)
    >>> win_count(30, 200)
    (11, 19, 9)
    """
    d = time ** 2 - 4 * record
    x1 = math.floor((time - math.sqrt(d)) / 2 + 1)
    x2 = math.ceil((time + math.sqrt(d)) / 2 - 1)

    return x2 - x1 + 1

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-6/input.txt"
    main(file_name)

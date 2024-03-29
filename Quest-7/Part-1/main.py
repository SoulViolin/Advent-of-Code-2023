import sys

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def main(file_name):
    lines = read_file(file_name)
    hands, bids = get_hands(lines)
    sorted_hands = sorted(zip(hands, bids), key=lambda x: (get_type(x[0]), [card_values[el] for el in x[0]]))

    total = sum([(rank + 1) * int(bid[1]) for rank, bid in enumerate(sorted_hands)])
    print(total)

def read_file(name):
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.readlines()

def get_hands(lines):
    hands = [line.split()[0] for line in lines]
    bids = [line.split()[1] for line in lines]
    return hands, bids

def get_type(hand):
    """
    >>> get_type("K2345")
    [1, 1, 1, 1, 1]
    >>> get_type("KK345")
    [2, 1, 1, 1]
    >>> get_type("KK677")
    [2, 2, 1]
    >>> get_type("J3222")
    [3, 1, 1]
    >>> get_type("KK777")
    [3, 2]
    >>> get_type("J2222")
    [4, 1]
    >>> get_type("22222")
    [5]
    """

    value_count = {}
    for card in hand:
        value = card[0]
        if value in value_count:
            value_count[value] += 1
        else:
            value_count[value] = 1

    return sorted(list(value_count.values()), reverse=True)

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-6/input.txt"
    main(file_name)

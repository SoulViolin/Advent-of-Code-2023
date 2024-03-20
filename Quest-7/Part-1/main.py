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
    1
    >>> get_type("KK345")
    2
    >>> get_type("KK677")
    3
    >>> get_type("J3222")
    4
    >>> get_type("KK777")
    5
    >>> get_type("J2222")
    6
    >>> get_type("22222")
    7
    """

    value_count = {}
    for card in hand:
        value = card[0]
        if value in value_count:
            value_count[value] += 1
        else:
            value_count[value] = 1

    if len(value_count) == 1:
        # Five of a kind
        return 7
    elif len(value_count) == 2:
        # Full house or Four of a kind
        if 2 in value_count.values():
            return 5
        else:
            return 6
    elif len(value_count) == 3:
        # Three of a kind or Two pair
        if 3 in value_count.values():
            return 4
        else:
            return 3
    elif len(value_count) == 4:
        # One pair
        return 2
    else:
        # High card
        return 1

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-6/input.txt"
    main(file_name)

import sys

card_values = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 12, 'K': 13, 'A': 14}

def main(file_name):
    lines = read_file(file_name)
    hands, bids = get_hands(lines)
    sorted_hands = sorted(zip(hands, bids), key=lambda x: (get_best_joker_value(x[0]), [card_values[el] for el in x[0]]))

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
    # >>> get_type("K2345")
    # [1, 1, 1, 1, 1]
    # >>> get_type("KK345")
    # [2, 1, 1, 1]
    # >>> get_type("KK677")
    # [2, 2, 1]
    # >>> get_type("J3222")
    # [3, 1, 1]
    # >>> get_type("KK777")
    # [3, 2]
    # >>> get_type("J2222")
    # [4, 1]
    # >>> get_type("22222")
    # [5]
    """

    value_count = {}
    for card in hand:
        value = card[0]
        if value in value_count:
            value_count[value] += 1
        else:
            value_count[value] = 1

    return sorted(list(value_count.values()), reverse=True)

def get_best_joker_value(hand):
    """
    >>> get_best_joker_value("J2222")
    [5]
    >>> get_best_joker_value("J3222")
    [4, 1]
    >>> get_best_joker_value("KKJ77")
    [3, 2]
    >>> get_best_joker_value("K3J22")
    [3, 1, 1]
    >>> get_best_joker_value("KJ345")
    [2, 1, 1, 1]

    >>> get_best_joker_value("J3J22")
    [4, 1]
    """
    hand_type = get_type(hand)

    for joker_value, _ in card_values.items():
        hand_with_joker = hand.replace('J', joker_value)
        best_value = get_type(hand_with_joker)
        if best_value > hand_type:
            hand_type = best_value

    return hand_type

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-6/input.txt"
    main(file_name)

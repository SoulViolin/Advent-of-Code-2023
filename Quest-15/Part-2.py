import sys

def main(file_name: str) -> None:
    input_strings = read_file(file_name)
    box_values = [hash_algorithm(input_string) for input_string in input_strings]
    boxes = process(box_values)
    focusing_power = get_power(boxes)

    print(focusing_power)

def read_file(name: str) -> list[str]:
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.read().splitlines()[0].rsplit(",")

def hash_algorithm(s):
    box = s.rsplit("=")[0].rsplit("-")[0]
    current_value = 0

    for char in box:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256

    return (current_value, s)

def process(box_values):
    boxes = {}

    for box, value in box_values:
        lens = value.rsplit("=")[0].rsplit("-")[0]
        focal_length = value.rsplit("=")[1] if len(value.rsplit("=")) > 1 else None
        if box not in boxes:
            boxes[box] = {}
            boxes[box][lens] = focal_length

        else:
            if "-" not in value:
                if lens not in boxes[box]:
                    boxes[box][lens] = focal_length
                else:
                    boxes[box][lens] = focal_length
            else:
                if lens in boxes[box]:
                    del boxes[box][lens]

    return boxes

def get_power(boxes):
    power = 0

    for box in boxes:
        for slot_index, slot in enumerate(boxes[box]):
            power += (int(box) + 1) * (int(slot_index) + 1) * int(boxes[box][slot])

    return power

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-15/input.txt"
    main(file_name)



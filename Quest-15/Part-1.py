import sys

def main(file_name: str) -> None:
    input_strings = read_file(file_name)
    hashed_values = [hash_algorithm(input_string) for input_string in input_strings]

    print(sum(hashed_values))

def read_file(name: str) -> list[str]:
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.read().splitlines()[0].rsplit(",")

def hash_algorithm(s):
    current_value = 0

    for char in s:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256

    return current_value

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-15/input.txt"
    main(file_name)

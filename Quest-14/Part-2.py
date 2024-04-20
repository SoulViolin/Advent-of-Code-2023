import sys

def main(file_name: str) -> None:
    lines = read_file(file_name)

def read_file(name: str) -> list[list[str]]:
    with open(file=name, mode="r", encoding="utf-8") as f:
        return [el.splitlines() for el in f.read().split("\n\n")]

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-14/input.txt"
    main(file_name)






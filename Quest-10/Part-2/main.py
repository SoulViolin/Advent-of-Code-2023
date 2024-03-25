import sys

def main(file_name):
    lines = read_file(file_name)

def read_file(name):
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.readlines()

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-8/input.txt"
    main(file_name)

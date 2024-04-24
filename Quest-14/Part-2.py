import sys

def main(file_name: str) -> None:
    lines = read_file(file_name)
    platform = rotate(rotate(rotate(lines)))
    platform = cycle_until_stable(platform)
    load_count = count_load(platform)
    print(load_count)

def read_file(name: str) -> list[str]:
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.read().splitlines()

def tilt(platform):
    return [tilt_row(row) for row in platform]

def tilt_row(row):
    stop = 0
    for i in range(len(row)):
        if row[i] == "#":
            stop = i + 1
        elif row[i] == "O":
            row[i] = "."
            row[stop] = "O"
            stop += 1
    return row

def count_load_row(row):
    load = 0
    for i in range(len(row)):
        if row[i] == "O":
            load += len(row) - i
    return load

def count_load(platform):
    return sum(count_load_row(row) for row in platform)

def rotate(platform):
    result = []
    for i in range(len(platform[0])):
        result.append([row[i] for row in reversed(platform)])
    return result

def cycle(platform):
    return rotate(tilt(rotate(tilt(rotate(tilt(rotate(tilt(platform))))))))

def make_snap(platform):
    return '\n'.join([''.join(row) for row in platform])

def cycle_until_stable(platform):
    cnt = 0
    seen = {}
    snap = make_snap(platform)
    while snap not in seen:
        seen[snap] = cnt
        platform = cycle(platform)
        cnt += 1
        snap = make_snap(platform)
    loop_start = seen[snap]
    loop_end = cnt
    iters = cheat(loop_start, loop_end, 1000000000)
    for _ in range(iters):
        platform = cycle(platform)
    return platform

def cheat(loop_start, loop_end, desired):
    return (desired - loop_end) % (loop_end - loop_start)

if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except:
        file_name = "Quest-14/input.txt"
    main(file_name)

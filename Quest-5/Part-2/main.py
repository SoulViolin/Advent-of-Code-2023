import sys
from dataclasses import dataclass

@dataclass
class Mapping:
    dest: int
    source: int
    length: int

def main(fileName):
    paras = read_file(fileName).rstrip("\n").split("\n\n")
    seeds = get_seeds(paras[0])
    maps = get_maps(paras[1:])

    min_location = min(get_locations(seeds, maps))

    print(min_location)

def read_file(name):
    with open(file=name, mode="r", encoding="utf-8") as f:
        return f.read()

def get_seeds(para):
    _, value = para.split(": ")
    seeds = [int(el) for el in value.split()]

    return seeds

def get_maps(paras):
    """
    >>> get_maps(['seed-to-soil map:\\n50 98 2\\n52 50 48', 'map:\\n50 98 2\\n52 50 48'])
    [[Mapping(dest=50, source=98, length=2), Mapping(dest=52, source=50, length=48)], [Mapping(dest=50, source=98, length=2), Mapping(dest=52, source=50, length=48)]]
    """
    maps = []

    for para in paras:
        lines = para.split("\n")
        values = []
        for line in lines[1:]:
            values.append(parse_line(line))
        maps.append(values)

    return maps

def parse_line(line):
    dest, source, length = map(int, line.split())
    return Mapping(dest, source, length)

def get_locations(seeds, maps):
    return [process_seed(seed, maps) for seed in seeds]

def process_seed(seed, maps_list):
    """
    # return location
    >>> process_seed(99, [[Mapping(dest=50, source=98, length=2), Mapping(dest=522, source=560, length=48)]])
    51
    >>> process_seed(99, [[Mapping(dest=50, source=98, length=2)], [Mapping(dest=0, source=15, length=37)]])
    36
    """
    result = seed

    for maps in maps_list:
        result = apply_maps(maps, result)

    return result

def apply_maps(maps, seed):
    """
    >>> apply_maps([Mapping(5, 7, 2)], 8)
    6
    >>> apply_maps([Mapping(5, 7, 2)], 1)
    1
    """
    for map in maps:
        result = apply_map(map, seed)
        if result is not None:
            return result

    return seed

def apply_map(map, seed):
    """
    >>> apply_map(Mapping(5, 7, 2), 8)
    6
    >>> apply_map(Mapping(5, 7, 2), 1) is None
    True
    """
    if  map.source <= seed < map.source + map.length:
        shift = seed - map.source
        return map.dest + shift

if __name__ == '__main__':
    try:
        fileName = sys.argv[1]
    except:
        fileName = "Quest-5/input.txt"
    main(fileName)

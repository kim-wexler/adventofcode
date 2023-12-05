import re, sys

f = open(sys.argv[1]).read().strip()

data = [[line.strip() for line in chunk.strip().splitlines()] for chunk in f.split("\n\n")]
seeds, *maps = [[re.findall("\\d+", line) for line in chunk] for chunk in data]
seeds = [int(x) for x in seeds[0]]

def convert_seed(seed, maps):

    val = None
    for map in maps:
        a, b, c = [int(x) for x in map]
        if b <= seed < b + c:
            if val:
                val = a + abs(seed-b)
            else:
                val = a + abs(seed-b)
            # print(map, seed)
            # return a + abs(seed-b)
    return val or seed

ans = None
for seed in seeds:
    x = seed
    for map in maps:
        _, *map = map
        x = convert_seed(x, map)
    ans = min(ans or x, x)
print(ans)

import sys
from functools import lru_cache

IN = sys.stdin.read()

G = dict()

for line in IN.strip().splitlines():
    a, b = line.strip().split(")")
    if a in G:
        G[a].append(b)
    else:
        G[a] = [b]

cache = {}
def solve(p):
    if p in cache:
        return cache[p]
    if p not in G:
        return 0
    cache[p] = sum(solve(pp) for pp in G[p]) + len(G[p])
    return cache[p]

print(sum(solve(p) for p in G.keys()))

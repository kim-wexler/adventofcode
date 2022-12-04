import sys

data = sys.stdin.read().strip().splitlines()

F = lambda x: ord(x) - 96 if x >= "a" else ord(x) - 38

pt1 = [set(l[:len(l)//2]) & set(l[len(l)//2:]) for l in data]
pt1ans = [next(map(F, r)) for r in pt1]

pt2 = [set.intersection(*[set(g) for g in data[i:i+3]]) for i in range(0, len(data), 3)]
pt2ans = [next(map(F, r)) for r in pt2]
print(sum(pt1ans), sum(pt2ans))

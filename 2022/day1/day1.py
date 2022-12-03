import sys

data = sys.stdin.read().split("\n\n")
ans = [sum([int(x) for x in line.strip().split("\n")]) for line in data]
ans.sort()
print(ans[-1], sum(ans[-3:]))

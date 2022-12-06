import sys

data = sys.stdin.read().strip()

def solve(data, n):
    return next(i+n for i in range(len(data)) if len(set(data[i:i+n])) == n)

print(solve(data, 4), solve(data, 14))

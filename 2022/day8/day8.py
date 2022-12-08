import sys

data = sys.stdin.read()
data = [list(line) for line in data.splitlines()]

def check_visible(i, j):
    if all(data[i][j] > data[k][j] for k in range(i)):
        return True
    if all(data[i][j] > data[i][k] for k in range(j)):
        return True
    if all(data[i][j] > data[k][j] for k in range(i+1, len(data))):
        return True
    if all(data[i][j] > data[i][k] for k in range(j+1, len(data))):
        return True
    return False

def find_score(i, j):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    ans = 1
    for (di, dj) in dirs:
        ix, jx = i, j
        dist = 0
        while True:
            ix += di
            jx += dj
            if ix < 0 or ix >= len(data) or jx < 0 or jx >= len(data):
                break
            elif data[ix][jx] < data[i][j]:
                dist += 1
            else:
                dist += 1
                break
        ans *= dist
    return ans

print(sum([check_visible(i, j) for i in range(len(data)) for j in range(len(data))]))
print(max([find_score(i, j) for i in range(len(data)) for j in range(len(data))]))

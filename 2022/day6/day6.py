import sys

data = sys.stdin.read().strip()

def solve(data, marker_len):
    for i in range(len(data)-marker_len):
        if len(set(data[i:i+marker_len])) == marker_len:
            return i + marker_len
    return 0

print(solve(data, 4), solve(data, 14))

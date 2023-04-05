import sys
from collections import deque
IN = sys.stdin.read()

G = [list(line) for line in IN.strip().splitlines()]
Qp1 = deque(((r, c), 0) for r in range(len(G)) for c in range(len(G[r])) if G[r][c] in ["S"])
Qp2 = deque(((r, c), 0) for r in range(len(G)) for c in range(len(G[r])) if G[r][c] in ["a", "S"])


def solve(Q, G):
    seen = set()
    while Q:
        (r, c), step = Q.popleft()
        if G[r][c] == "E":
            return step
        if (r, c) in seen:
            continue
        seen.add((r, c))
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= dr+r < len(G) and 0 <= dc+c < len(G[0]):
                pos = ord("a") if G[r][c] == "S" else ord(G[r][c])
                nbr = ord("z") if G[dr+r][dc+c] == "E" else ord(G[dr+r][dc+c])
                if pos - nbr >= -1:
                    Q.append(((dr+r, dc+c), step + 1))
    return False

print(solve(Qp1, G))
print(solve(Qp2, G))

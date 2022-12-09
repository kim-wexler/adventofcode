import sys

data = sys.stdin.read().splitlines()
data = [line.split(" ") for line in data]

def set_pos(D):
    for i in range(len(D)-2, -1, -1):
        x, y = D[i+1]
        dx, dy = D[i]
        if abs(x-dx) > 1 or abs(y-dy) > 1:
            if x > dx:
                dx += 1
            elif x < dx:
                dx -= 1
            if y > dy:
                dy += 1
            elif y < dy:
                dy -= 1
            D[i] = (dx, dy)

tail = set()
tail2 = set()
x = y = 0
dx = dy = 0
pos = [(0,0)] * 9
for d in data:
    (a, b) = d[0], int(d[1])
    for i in range(b):
        if a == "R":
            x += 1
        if a == "L":
            x -= 1
        if a == "U":
            y += 1
        if a == "D":
            y -= 1
        if abs(x-dx) > 1 or abs(y-dy) > 1:
            if x > dx:
                dx += 1
            elif x < dx:
                dx -= 1
            if y > dy:
                dy += 1
            elif y < dy:
                dy -= 1
            pos[-1] = (dx, dy)
            set_pos(pos)
        tail.add(pos[0])
        tail2.add(pos[-1])
print(len(tail), len(tail2))

# X = 4, 2
# T = 3, 0

# X = 2, 2
# T = 4, 1

X = 4, 1
T = 3, 0

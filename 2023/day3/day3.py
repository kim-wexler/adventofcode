import sys, math

f = open(sys.argv[1]).read().strip()

sch = [list(line) for line in f.splitlines()]
gears = [(i, j) for i in range(len(sch)) for j in range(len(sch)) if sch[i][j] == "*"]

def check_adj(r, c, schematic):
    adj = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
    for rr, cc in adj:
        if 0 <= rr+r < len(schematic) and 0 <= cc+c < len(schematic):
            if schematic[rr+r][cc+c] != "." and not schematic[rr+r][cc+c].isdigit():
                return True
    return False

num_coords = []
for i in range(len(sch)):
    num = []
    for j in range(len(sch[i])):
        if not sch[i][j].isdigit() and num:
            num_coords.append(num)
            num = []
        if sch[i][j].isdigit():
            num.append((i, j))
    if num:
        num_coords.append(num)

ans = ans2 = 0
for num in num_coords:
    if any(check_adj(r, c, sch) for r,c in num):
        ans += int("".join(sch[r][c] for r,c in num))

for i, j in gears:
    adj_nums = []
    adj = [(i+ii, j+jj) for ii in [0, -1, 1] for jj in [0, -1, 1] if (ii, jj) != (0, 0)]
    for num in num_coords:
        if any((r, c) in num for r,c in adj):
            adj_nums.append(int("".join(sch[r][c] for r,c in num)))
    if len(adj_nums) == 2:
        ans2 += math.prod(adj_nums)

print(ans, ans2)

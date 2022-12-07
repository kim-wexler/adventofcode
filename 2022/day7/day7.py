import sys, random
from collections import defaultdict

data = sys.stdin.read().strip()
data = [line.split(" ") for line in data.splitlines()]
dirsizes = defaultdict(int)

pwd = []
for line in data:
    if line[1] == "cd":
        if line[2] == "..":
            pwd.pop()
        else:
            if line[2] not in dirsizes:
                pwd.append(line[2])
            else:
                d = line[2] + str(random.randint(1, 100000))
                pwd.append(d)
    elif line[1] == "ls":
        continue
    else:
        if line[0] != "dir":
            for p in pwd:
                dirsizes[p] += int(line[0])

print(sum(d for d in dirsizes.values() if d <= 100000))
need = 30000000 - (70000000 - dirsizes["/"])
print(min(d for d in dirsizes.values() if d > need))

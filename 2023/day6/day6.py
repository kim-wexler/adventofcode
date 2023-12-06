import re, sys

f = open(sys.argv[1]).read().strip()

times, dists = [[int(x) for x in re.findall("\\d+", line)] for line in f.splitlines()]
p2time, p2record = [int("".join(re.findall("\\d+", line))) for line in f.splitlines()]

ans = 1
for i in range(len(times)):
    t = times[i]
    record = dists[i]
    arr = [(t - j) * j for j in range(t+1) if (t - j) * j > record]
    ans *= len(arr)
print(ans)

t = 0
while t * (p2time - t) < p2record:
    t += 1
print(p2time - (2 * t) + 1)

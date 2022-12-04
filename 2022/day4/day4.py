import sys, re
data = sys.stdin.read().strip().splitlines()
bounds = [[int(x) for x in re.findall("\d+", bound)] for bound in data]
ans1 = [(1 if a <= c <= d <= b or c <= a <= b <= d else 0) for (a,b,c,d) in bounds]
ans2 = [(1 if a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d else 0) for (a,b,c,d) in bounds]
print(sum(ans1), sum(ans2))

import sys

data = sys.stdin.read().strip().split("\n\n")
ins = [d.split(" ") for d in data[1].split("\n")]
ins = [(int(d[1]), int(d[3]), int(d[5])) for d in ins]
# cargo = ["ZN", "MCD", "P"]
cargo = ["GTRW", "GCHPMSVW", "CLTSGM", "JHDMWRF", "PQLHSWFJ", "PJDNFMS", "ZBDFGCSJ", "RTB", "HNWLC"]
cargo = [list(c) for c in cargo]

for (move, frm, to) in ins:
    new = []
    for _ in range(move):
        new.insert(0, cargo[frm-1].pop())
        # cargo[to-1].append(cargo[frm-1].pop())
    cargo[to-1] += new
ans = "".join([x[-1] for x in cargo])
print(ans)

import sys

IN = sys.stdin.read()
instructions = []
for line in IN.strip().splitlines():
    signal, dst = line.strip().split(" -> ")
    signal = signal.split(" ")
    instructions.append((signal, dst))

def parse_signal(signal, D):
    if signal.isnumeric():
        return int(signal)
    return D.get(signal)

def solve(instructions, D):
    BITS = 65536
    while instructions:
        signal, dst = instructions.pop(0)
        if len(signal) == 1:
            sig_a = parse_signal(signal[0], D)
            if sig_a != None:
                D[dst] = sig_a
            else:
                instructions.append((signal, dst))
        elif len(signal) == 2:
            sig_a = parse_signal(signal[1], D)
            if sig_a != None:
                D[dst] = ~sig_a % BITS
            else:
                instructions.append((signal, dst))
        else:
            sig_a = parse_signal(signal[0], D)
            sig_b = parse_signal(signal[2], D)
            op = signal[1]
            if op == "AND" and sig_a != None and sig_b != None:
                D[dst] = sig_a & sig_b % BITS
            elif op == "OR" and sig_a != None and sig_b != None:
                D[dst] = sig_a | sig_b % BITS
            elif op == "LSHIFT" and sig_a != None and sig_b != None:
                D[dst] = sig_a << sig_b % BITS
            elif op == "RSHIFT" and sig_a != None and sig_b != None:
                D[dst] = sig_a >> sig_b % BITS
            else:
                instructions.append((signal, dst))

    return D["a"]

pt1 = solve(instructions.copy(), dict())
pt2_instructions = [ins if ins[1] != "b" else ([str(pt1)], "b") for ins in instructions]
pt2 = solve(pt2_instructions, dict())
print(pt1, pt2)

from collections import defaultdict

f = open("input.txt", "r")
lines = f.readlines()

registers = defaultdict(int)

for line in lines:
    reg, inst, amount, iff, regc, op, val = line.split()

    if eval("registers[reg] " + op + val):
        if inst == "inc":
            registers[reg] += int(amount)
        else:
            registers[reg] -= int(amount)

print("Solutions: {0}".format(max(registers.values())))
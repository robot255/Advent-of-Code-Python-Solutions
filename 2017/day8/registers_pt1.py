from collections import defaultdict

f = open("input.txt", "r")
lines = f.readlines()

ht = {}
registers = defaultdict(lambda:0, ht)

for line in lines:
    tokens = line.split()
    register = tokens[0]
    change = tokens[1]
    amount = int(tokens[2])
    check_register = tokens[4]
    operation = tokens[5]
    value = int(tokens[6])

    if operation == "!=" and registers[check_register] == value:
        continue
    if operation == "==" and registers[check_register] != value:
        continue
    if operation == ">" and registers[check_register] < value:
        continue
    if operation == "<" and registers[check_register] > value:
        continue
    if operation == ">=" and registers[check_register] < value:
        continue
    if operation == "<=" and registers[check_register] > value:
        continue

    if change == "inc":
        registers[register] += amount
    else:
        registers[register] -= amount

print("Solutions: {0}".format(max(registers.values())))
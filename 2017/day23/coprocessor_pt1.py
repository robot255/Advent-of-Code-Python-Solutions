from collections import defaultdict

f = open("input.txt", "r")
instructions = f.readlines()

sound_played = None
registers = defaultdict(int)
loc = 0
mul_count = 0

def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

registers['a'] = 1

while loc < len(instructions):
    instruction = instructions[loc]
    action = instruction.split()

    if is_digit(action[2]):
        value = int(action[2])
    else:
        value = registers[action[2]]

    if action[0] == 'jnz':
        if is_digit(action[1]):
            x = int(action[1])
        else:
            x = registers[action[1]]

    if action[0] == "set":
        registers[action[1]] = value
    elif action[0] == "sub":
        registers[action[1]] -= value
    elif action[0] == "mul":
        registers[action[1]] *= value
        mul_count += 1
    elif action[0] == "jnz" and x != 0:
        loc += value
        continue
    loc += 1

print("Solution: {0}".format(mul_count))
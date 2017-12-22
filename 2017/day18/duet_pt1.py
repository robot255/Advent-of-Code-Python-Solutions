from collections import defaultdict

f = open("input.txt", "r")
instructions = f.readlines()

sound_played = None
registers = defaultdict(int)
loc = 0


def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


while True:
    instruction = instructions[loc]
    action = instruction.split()

    if len(action) == 3:
        if is_digit(action[2]):
            value = int(action[2])
        else:
            value = registers[action[2]]
    else:
        if is_digit(action[1]):
            value = int(action[1])
        else:
            value = registers[action[1]]

    if action[0] == "snd":
        sound_played = registers[action[1]]
    elif action[0] == "set":
        registers[action[1]] = value
    elif action[0] == "add":
        registers[action[1]] += value
    elif action[0] == "mul":
        registers[action[1]] *= value
    elif action[0] == "mod":
        registers[action[1]] %= value
    elif action[0] == "rcv" and registers[action[1]] != 0:
        break
    elif action[0] == "jgz" and registers[action[1]] > 0:
        loc += value
        continue
    loc += 1

print("Solution: {0}".format(sound_played))
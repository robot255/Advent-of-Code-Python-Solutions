from collections import defaultdict

f = open("input.txt", "r")
commands = f.readlines()

lights = defaultdict(int)

count = 0
for command in commands:
    count += 1
    print("command {0}".format(count))
    tokens = command.split()
    if len(tokens) == 5:
        action = tokens[1]
        x_start = int(tokens[2].split(",")[0])
        y_start = int(tokens[2].split(",")[1])
        x_end = int(tokens[4].split(",")[0])
        y_end = int(tokens[4].split(",")[1])
    else:
        action = "toggle"
        x_start = int(tokens[1].split(",")[0])
        y_start = int(tokens[1].split(",")[1])
        x_end = int(tokens[3].split(",")[0])
        y_end = int(tokens[3].split(",")[1])

    for x in range(x_start, x_end + 1):
        for y in range(y_start, y_end + 1):
            if action == "toggle":
                lights[(x, y)] += 2
            elif action == "off":
                lights[(x, y)] = max(0, lights[(x, y)] - 1)
            elif action == "on":
                lights[(x, y)] += 1

print("Solution: {0}".format(sum(lights.values())))


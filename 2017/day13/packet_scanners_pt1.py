from collections import defaultdict
from collections import deque

f = open("input.txt", "r")
lines = f.readlines()

# lines = ["0: 3",
#             "1: 2",
#             "4: 4",
#             "6: 4"]

system = defaultdict()
dir = defaultdict()

for level in lines:
    r, depth = level.split(":")
    r = int(r)
    depth = int(depth)
    system[r] = [1] + ([0] * (depth - 1))
    dir[r] = "UP"

severity = 0

for layer in range(max(system.keys()) + 1):
    if layer in system and system[layer][0] == 1:
        severity += layer * len(system[layer])

    for i in range(max(system.keys()) + 1):
        if i in system and i in dir:
            print(system[i])
            loc = system[i].index(1)
            if dir[i] == "UP" and loc + 1 < len(system[i]):
                system[i][loc] = 0
                system[i][loc + 1] = 1
                continue
            elif dir[i] == "UP" and loc + 1 >= len(system[i]):
                dir[i] = "DOWN"
                system[i][loc] = 0
                system[i][loc - 1] = 1
                continue
            elif dir[i] == "DOWN" and loc - 1 >= 0:
                system[i][loc] = 0
                system[i][loc - 1] = 1
            elif dir[i] == "DOWN" and loc - 1 < 0:
                dir[i] = "UP"
                system[i][loc] = 0
                system[i][loc + 1] = 1

print("Solution: {0}".format(severity))







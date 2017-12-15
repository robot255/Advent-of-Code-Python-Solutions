import time

START = time.time()

data = open("input.txt", "r")
rows = data.read().strip().split("\n")

valDict = dict()

for row in rows:
    rowS = row.split(" ")
    valDict[int(rowS[0][:-1])] = int(rowS[-1])

caught = False
for delay in iter(range(10, 10 ** 7)):
    caught = False
    for i in valDict.keys():
        if (i + delay) % (2 * valDict[i] - 2) == 0:
            print("caught {0}".format(delay))
            caught = True
            break
    if not caught:
        print(delay)
        break





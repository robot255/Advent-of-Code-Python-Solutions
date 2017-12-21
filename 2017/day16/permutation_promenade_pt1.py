from collections import deque


f = open("input.txt", "r")
lines = f.read()
moves = lines.split(",")

line_dance = deque('abcdefghijklmnop')
# line_dance = deque('abcde')
# moves = ['s1', 'x3/4', 'pe/b']

for move in moves:
    print("move: {0} line:{1}".format(move, line_dance))

    if move.startswith("s"):
        rotation = int(move[1:])
        line_dance.rotate(rotation)

    if move.startswith("x"):
        locs = move[1:].split("/")
        loc1 = int(locs[0])
        loc2 = int(locs[1])

        temp = line_dance[loc1]
        line_dance[loc1] = line_dance[loc2]
        line_dance[loc2] = temp

    if move.startswith("p"):
        dances = move[1:].split("/")
        loc1 = line_dance.index(dances[0])
        loc2 = line_dance.index(dances[1])

        temp = line_dance[loc1]
        line_dance[loc1] = line_dance[loc2]
        line_dance[loc2] = temp
    print("after: {0} line:{1}".format(move, line_dance))
    print("--------")

print("Solution: {0}".format("".join(line_dance)))

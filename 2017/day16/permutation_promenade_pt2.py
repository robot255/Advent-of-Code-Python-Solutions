from collections import deque


f = open("input.txt", "r")
lines = f.read()
moves = lines.split(",")

line_dance = deque('abcdefghijklmnop')

seen = {}
loop_count = 0
seen_duplicate = False
billion_loops = None

#gnflbkojhicpmead
while True:
    start_dance = "".join(line_dance)

    if start_dance in seen:
        line_dance = deque(seen[start_dance])

        if billion_loops == 0:
            break

        if seen_duplicate:
            billion_loops -= 1
        else:
            seen_duplicate = True
            billion_loops = (1000000000 % loop_count)
    loop_count += 1

    for move in moves:
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

    seen[start_dance] = "".join(line_dance)
print("Solution: {0} {1}".format("".join(line_dance), loop_count))

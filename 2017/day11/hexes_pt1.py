import math
"""
  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \
https://www.redblobgames.com/grids/hexagons/
"""


f = open("input.txt", "r")
input = f.read()

x = 0
y = 0
z = 0
dist = []
for d in input.split(","):
    if d == "n":
        y += 1
        z -= 1
    elif d == "s":
        y -= 1
        z += 1
    elif d == "ne":
        x += 1
        z -= 1
    elif d == "sw":
        x -= 1
        z += 1
    elif d == "nw":
        x -= 1
        y += 1
    elif d == "se":
        x += 1
        y -= 1
    dist.append((abs(x) + abs(y) + abs(z)) / 2)
total_distance = (abs(x) + abs(y) + abs(z)) / 2
print("Solution Part 1: {0}".format(total_distance))
print("Solution Part 2: {0}".format(max(dist)))




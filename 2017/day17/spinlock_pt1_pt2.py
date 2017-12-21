from collections import deque

input = 359

def spin(inserts):
    spinlock = deque([0])
    for i in range(1, inserts + 1):
        spinlock.rotate(-input)
        spinlock.append(i)
    return spinlock

part1 = spin(2017)
part2 = spin(50_000_000)
print("solution 1: {0}".format(part1[0]))
print("solution 2: {0}".format(part2[part2.index(0) + 1]))

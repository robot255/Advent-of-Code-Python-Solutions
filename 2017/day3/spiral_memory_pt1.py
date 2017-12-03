import math
import numpy as np


NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0) # directions
turn_right = {S: E, W: S, NORTH: W, E: NORTH} # old -> new direction

def spiral(width, height):
    if width < 1 or height < 1:
        raise ValueError
    x, y = width // 2, height // 2 # start near the center
    dx, dy = S # initial direction
    matrix = [[None] * width for _ in range(height)]
    count = 0
    while True:
        matrix[y][x] = count
        count += 1# visit
        # try to turn right
        new_dx, new_dy = turn_right[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
            matrix[new_y][new_x] is None): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix # nowhere to go

def print_matrix(matrix):
    width = len(str(max(el for row in matrix for el in row if el is not None)))
    fmt = "{:0%dd}" % width
    for row in matrix:
        print(" ".join("_"*width if el is None else fmt.format(el) for el in row))


if __name__ == "__main__":

    value = 289326


    side = int(math.floor(math.sqrt(value))) + 2

    m = spiral(side,side)
    a = np.array(m)
    one_loc = np.where(a == 1)
    val_loc = np.where(a == value)

    print(one_loc)
    print(val_loc)

    distance = abs(val_loc[0][0] - one_loc[0][0]) + abs(val_loc[1][0] - one_loc[1][0])

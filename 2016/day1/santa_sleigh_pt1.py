def santa_move(directions):
    x = 0
    y = 0

    cur_dir = "NORTH"

    transition_l = {"NORTH": "WEST",
                    "EAST": "NORTH",
                    "WEST": "SOUTH",
                    "SOUTH": "EAST"}
    transition_r = {"NORTH": "EAST",
                    "EAST": "SOUTH",
                    "WEST": "NORTH",
                    "SOUTH": "WEST"}

    for direction in directions:
        direction = direction.strip()
        turn = direction[0]
        distance = int(direction[1:])

        if turn == "L":
            cur_dir = transition_l[cur_dir]
        else:
            cur_dir = transition_r[cur_dir]

        if cur_dir == "NORTH":
            y += distance
        if cur_dir == "SOUTH":
            y -= distance
        if cur_dir == "EAST":
            x += distance
        if cur_dir == "WEST":
            x -= distance

    distance = abs(x - 0) + abs(y - 0)
    return distance


if __name__ == "__main__":
    f = open("input.txt", "r")
    content = f.read()
    content = content.split(",")
    solution = santa_move(content)

    print("Solution: {0}".format(solution))




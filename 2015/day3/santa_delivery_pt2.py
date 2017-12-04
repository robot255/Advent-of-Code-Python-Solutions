def houses_delivered(directions):
    x = 0
    y = 0

    visited_houses = set()
    for direction in directions:

        if direction == "^":
            y += 1

        if direction == "v":
            y -= 1

        if direction == "<":
            x -= 1

        if direction == ">":
            x += 1

        visited_houses.add((x ,y))
    return visited_houses


def santa_deliver_map(directions):

    santa_houses = houses_delivered(directions[::2])
    robo_santa_houses = houses_delivered(directions[1::2])

    houses = santa_houses | robo_santa_houses

    return len(houses)


if __name__ == "__main__":
    f = open("input.txt", "r")
    directions = f.read()
    houses = santa_deliver_map(directions)

    print("Solutions: {0}".format(houses))


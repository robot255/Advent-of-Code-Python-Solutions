

def santa_deliver_map(directions):
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

        visited_houses.add((x,y))

    return len(visited_houses)


if __name__ == "__main__":
    f = open("input.txt", "r")
    directions = f.read()
    houses = santa_deliver_map(directions)

    print("Solutions: {0}".format(houses))


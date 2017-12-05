

if __name__ == "__main__":
    f = open("input.txt", "r")
    lines = f.readlines()
    lines = [int(line) for line in lines]

    location = 0
    steps = 0
    while True:
        if location >= len(lines):
            break

        lines[location] += 1
        location += lines[location] - 1
        steps += 1

    print("Solution: {0}".format(steps))


if __name__ == "__main__":
    f = open("input.txt", "r")
    lines = f.readlines()
    lines = [int(line) for line in lines]

    location = 0
    steps = 0
    while location >= 0 and location < len(lines):
        #print("{0} {1} ".format(lines, location))
        value = lines[location]
        if value >= 3:
            lines[location] -= 1
        else:
            lines[location] += 1
        location += value
        steps += 1


    print("Solution: {0}".format(steps))
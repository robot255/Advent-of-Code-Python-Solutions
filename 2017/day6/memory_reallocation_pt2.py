def redistribute(memory):
    patterns = {}

    redist = 0
    while tuple(memory) not in patterns:
        print("{0} {1}".format(memory, redist))
        patterns[tuple(memory)] = redist
        redist += 1
        i, m = max(enumerate(memory), key=lambda k: k[1])

        memory[i] = 0
        for j in range(m):
            memory[(i+j+1)%len(memory)] += 1

    first = patterns[tuple(memory)]
    return redist - first


if __name__ == "__main__":
    f = open("input.txt", "r")
    lines = f.read().split()
    banks = [int(i) for i in lines]
    result = redistribute(banks)

    print("Solution: {0}".format(result))
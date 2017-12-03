if __name__ == '__main__':
    f = open("checksum.txt", "r")
    content = f.readlines()
    content = [line.split() for line in content]
    int_contents = []

    total = 0
    for i in content:
        line_of_ints = [int(x) for x in i]
        total += max(line_of_ints) - min(line_of_ints)

    print("Solution: {0}".format(total))
if __name__ == '__main__':
    f = open("checksum.txt", "r")
    content = f.readlines()
    content = [line.split() for line in content]
    int_contents = []

    total = 0
    for i in content:
        line = [int(x) for x in i]

        for idx in range(len(line)):
            for idx2 in range(len(line)):
                if idx != idx2 and (line[idx] % line[idx2]) == 0:
                    total += line[idx] / line[idx2]

    print("Solution: {0}".format(total))
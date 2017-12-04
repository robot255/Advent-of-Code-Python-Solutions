def is_nice(string):
    pass

if __name__ == "__main__":
    f = open("input.txt", "r")
    strings = f.readlines()

    total_nice = 0
    for string in strings:
        if is_nice(string):
            total_nice += 1

    print("Solutions: {0}".format(total_nice))


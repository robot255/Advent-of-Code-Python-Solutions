def is_nice(line):
    has_duplicate = False
    for i in range(len(line)-2):
        if line.count(line[i:i+2]) >= 2:
            has_duplicate = True
            break
    if not has_duplicate:
        return False

    for i in range(len(line) - 2):
        if line[i] == line[i+2]:
            return True

    return False


if __name__ == "__main__":
    f = open("input.txt", "r")
    strings = f.readlines()

    # strings = ["qjhvhtzxzqqjkmpb",
    #            "xxyxx",
    #            "uurcxstgmygtbstg",
    #            "ieodomkazucvgmuy"]

    total_nice = 0
    for string in strings:
        print("string {0} {1}".format(string, is_nice(string)))
        if is_nice(string):
            total_nice += 1

    print("Solutions: {0}".format(total_nice))


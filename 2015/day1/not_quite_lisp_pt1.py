

def stack(input):
    stairs = []
    for i in input:
        if not stairs:
            stairs.append(i)
            continue

        if stairs[-1] == i:
            stairs.append(i)
            continue

        if stairs[-1] != i:
            stairs.pop()
            continue

    floor = len(stairs)

    if floor == 0 or stairs[0] != ")":
        return floor

    return floor * -1

if __name__ == "__main__":
    f = open("input.txt", "r")
    content = f.read()
    result = stack(content)

    print("Solution {0}".format(result))
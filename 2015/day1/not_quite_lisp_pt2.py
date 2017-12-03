

def stack(input):
    stairs = []
    for idx, i in enumerate(input):
        if not stairs:
            if i == ")":
                return idx + 1
            stairs.append(i)
            continue

        if stairs[-1] == i:
            stairs.append(i)
            continue

        if stairs[-1] != i:
            stairs.pop()
            continue


if __name__ == "__main__":
    f = open("input.txt", "r")
    content = f.read()
    result = stack(content)

    print("Solution {0}".format(result))
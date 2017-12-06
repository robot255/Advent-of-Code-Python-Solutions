def is_triangle(l, w, h):
    if l + w <= h:
        return False
    if l + h <= w:
        return False
    if w + h <= l:
        return False
    return True


if __name__ == "__main__":
    f = open("input.txt", "r")
    contents = f.readlines()
    triangles = 0

    rows = [[], [], []]
    for i in contents:
        dimensions = [int(x) for x in i.split()]
        for j in range(3):
            rows[j].append(dimensions[j])

    for s in range(0, 3):
        for i in range(0, 1635, 3):
            if is_triangle(rows[s][i], rows[s][i+1], rows[s][i+2]):
                triangles += 1

    print("Solution: {0}".format(triangles))

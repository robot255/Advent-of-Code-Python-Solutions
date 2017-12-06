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

    for i in contents:
        dimensions = [int(x) for x in i.split()]
        if is_triangle(*dimensions):
            triangles += 1

    print("Solution: {0}".format(triangles))

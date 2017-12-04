def calculate_wrapping_paper(l, w, h):
    side1 = l * w
    side2 = l * h
    side3 = w * h

    area = (2 * side1) + (2 * side2) + (2 * side3)
    extra = min(side1, side2, side3)

    return area + extra


if __name__ == "__main__":
    f = open("input.txt", "r")
    presents = f.readlines()

    total_wrapping_paper = 0
    for present in presents:
        dimensions = present.split("x")
        dimensions = [int(i.strip()) for i in dimensions]

        total_wrapping_paper += calculate_wrapping_paper(*dimensions)

    print("Solution {0}".format(total_wrapping_paper))




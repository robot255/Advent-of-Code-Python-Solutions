def calculate_ribbon(l, w, h):
    volume = l * w * h

    l = [l,w,h]
    l.sort()
    bow = (l[0] * 2) + (l[1] * 2)

    return volume + bow


if __name__ == "__main__":
    f = open("input.txt", "r")
    presents = f.readlines()

    total_ribbon = 0
    for present in presents:
        dimensions = present.split("x")
        dimensions = [int(i.strip()) for i in dimensions]

        total_ribbon += calculate_ribbon(*dimensions)

    print("Solution {0}".format(total_ribbon))




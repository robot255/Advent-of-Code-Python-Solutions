import re
import operator
from collections import Counter
from itertools import groupby


if __name__ == "__main__":
    f = open("input.txt", "r")
    contents = f.readlines()

    valid = 0
    # contents = ["aaaaa-bbb-z-y-x-123[abxyz]\n",
    #             "a-b-c-d-e-f-g-h-987[abcde]\n",
    #             "not-a-real-room-404[oarel]\n",
    #             "totally-real-room-200[decoy]\n"]
    #contents = ["qzmt-zixmtkozy-ivhz-343[abcde]"]
    for content in contents:
        tokens = re.split(r'-|\[|]', content.strip())
        tokens[::-1]

        encrypted = tokens[0:-3]
        sector = int(tokens[-3])
        check_sum = tokens[-2]

        decoded = ""
        for character in "-".join(encrypted):
            if character == "-":
                decoded += "-"
            else:
                offset = ord(character) - ord("a")
                decoded += chr(ord("a") + ((sector + offset) % 26))
        print("decoded: {0} => {1}".format(decoded, sector))
    print("Solutions: {0}".format(valid))
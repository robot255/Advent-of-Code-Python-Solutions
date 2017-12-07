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

    for content in contents:
        tokens = re.split(r'-|\[|]', content.strip())
        tokens[::-1]

        encrypted = "".join(tokens[0:-3])
        sector = int(tokens[-3])
        check_sum = tokens[-2]

        c = Counter(encrypted)
        five_most_common = c.most_common()
        ordered = []
        for k, group in groupby(five_most_common, key=lambda x: x[1]):
            ordered.extend(sorted(list(group)))

        hash = ""
        for i in range(5):
            hash += ordered[i][0]

        if check_sum == hash:
            valid += sector

    print("Solutions: {0}".format(valid))
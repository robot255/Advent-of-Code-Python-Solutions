import numpy as np
import copy
import binhex
from functools import reduce


input = "hwlqcszp"

def hash_knot(input):
    skip_sizes = [ord(i) for i in input] + [17, 31, 73, 47, 23]
    original_list = [ i for i in range(256)]

    index = 0
    skip_size = 0

    for round in range(64):
        for skip in skip_sizes:
            transition_list = copy.deepcopy(original_list)

            select_reversed = [(index + i) % len(original_list) for i in range(skip)][::-1]
            for i in range(skip):
                original_list[(index + i) % len(original_list)] = transition_list[select_reversed[i]]
            index = (index + skip_size + skip) % len(original_list)
            skip_size +=1

    xor_result = ""
    for j in range(0, 16):
        xor_result += '%02x' % reduce((lambda x,y: x ^ y), original_list[16*j:16+16*j])

    return xor_result

rows = []

binary_total = 0
for i in range(0,128):
    hash = "{0}-{1}".format(input, i)
    result = hash_knot(hash)
    bin_hash = bin(int(result, 16))[2:].zfill(128)
    binary_total += bin_hash.count('1')

    rows.append(list(map(int, bin_hash)))

    print("hash: {0} result:{1} bin:{2} total:{3}".format(hash, result,
                                                          bin_hash.count('1'),
                                                          binary_total))
seen = set()
n = 0

def depth_first_search(i,j):
    if ((i, j)) in seen:
        return
    if not rows[i][j]:
        return
    seen.add((i, j))
    if i > 0:
        depth_first_search(i-1, j)
    if j > 0:
        depth_first_search(i, j-1)
    if i < 127:
        depth_first_search(i+1,j)
    if j < 127:
        depth_first_search(i, j+1)

for i in range(128):
    for j in range(128):
        if (i,j) in seen:
            continue
        if not rows[i][j]:
            continue
        n += 1
        depth_first_search(i, j)

print("Solution: {0}".format(n))
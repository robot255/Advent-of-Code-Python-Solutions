import operator as op
from functools import reduce
import copy
f = open("input.txt", "r")
input = f.read()

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

xor_result = []
for j in range(0, 16):
    xor_result.append( '%02x' % reduce((lambda x,y: x ^ y), original_list[16*j:16+16*j]))

print(''.join(xor_result))
print(original_list)
print(original_list[0] * original_list[1])




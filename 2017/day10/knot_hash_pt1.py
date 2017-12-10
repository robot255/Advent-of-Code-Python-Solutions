import copy
f = open("input.txt", "r")
input = f.read()

skip_sizes = [int(i) for i in input.split(",")]
original_list = [ i for i in range(256)]
#
# skip_sizes = [3, 4, 1, 5]
# original_list = [ i for i in range(5)]

index = 0
skip_size = 0
for skip in skip_sizes:
    print(original_list)
    transition_list = copy.deepcopy(original_list)

    select_reversed = [(index + i) % len(original_list) for i in range(skip)][::-1]
    for i in range(skip):
        original_list[(index + i) % len(original_list)] = transition_list[select_reversed[i]]
    index = (index + skip_size + skip) % len(original_list)
    skip_size +=1

print(original_list)
print(original_list[0] * original_list[1])




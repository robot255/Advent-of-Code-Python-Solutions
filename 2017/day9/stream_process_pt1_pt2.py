import re

f = open("input.txt", "r")
input = f.read()


filtered = ""
garbage_count = 0
in_garbage = False
skip_char = False
depth = 0
score = 0
for i in input:
    if in_garbage:
        if skip_char == True:
            skip_char = False
            continue
        elif i == "!":
            skip_char = True
        elif i == ">":
            in_garbage = False
        else:
            garbage_count += 1
    else:
        if i == "{":
            depth += 1
        elif i == "}":
            score += depth
            depth -= 1
        elif i == "<":
            in_garbage = True

print("part 1: {0} part 2: {1}".format(score, garbage_count))


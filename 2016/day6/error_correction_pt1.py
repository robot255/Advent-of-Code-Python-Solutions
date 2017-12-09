from collections import Counter
f = open("input.txt", "r")
contents = f.readlines()

chars = [ [] for i in contents[0]]

for line in contents:
    for idx, i in enumerate(line):
        chars[idx].append(i)

result = ""
for a in chars:
    c = Counter(a)
    result += c.most_common(1)[0][0]

print(result)
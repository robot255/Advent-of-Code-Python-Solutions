divid_value = 2147483647

def generator(factor, seed, multiples):
    value = (factor * seed) % divid_value
    yield value
    while True:
        value = (value * factor) % divid_value
        if value % multiples == 0:
            yield value

gen_a = generator(16807, 699, 4)
gen_b = generator(48271, 124, 8)

matches = 0
for i in range(5000000):
    print(i)
    a = next(gen_a)
    b = next(gen_b)

    bin_a = bin(a)[2:].zfill(32)
    bin_b = bin(b)[2:].zfill(32)

    if bin_a[16:32] == bin_b[16:32]:
        matches += 1

print("Solutions: {0}".format(matches))
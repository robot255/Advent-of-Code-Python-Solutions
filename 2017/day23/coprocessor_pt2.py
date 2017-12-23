def is_prime(a):
    return all(a % i for i in range(2, a))


b = 109300
c = 126300
h = 0

for b in range(109300, c + 1, 17):
    if not is_prime(b):
        h += 1

print(h)

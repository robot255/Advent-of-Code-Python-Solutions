import numpy as np


f = open("input.txt", "r")
particles = f.readlines()

start_p = [0, 0, 0]

scaler_product = {}

for idx, particle in enumerate(particles):
    p, v, a = particle.split()
    p = p.replace("p=<", "").strip(">,").split(",")
    p = [int(i) for i in p]

    v = v.replace("v=<", "").strip(">,").split(",")
    v = [int(i) for i in v]

    a = tuple(a.replace("a=<", "").strip(">,").split(","))
    a = [int(i) for i in a]

    unit = (v[0] * v[0]) + (v[1] * v[1]) + (v[2] * v[2])
    u = [ j / (unit * unit) for j in v]

    scaler_product[idx] = abs(np.dot(u, a))

print("solution: {0}".format(min(scaler_product, key=scaler_product.get)))
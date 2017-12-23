from collections import defaultdict

f = open("input.txt", "r")

class Particle(object):
  def __init__(self, p, v, a):
    self.p = p
    self.v = v
    self.a = a

  def step(self):
    for i in range(3):
      self.v[i] += self.a[i]
      self.p[i] += self.v[i]


parts = {}
i = 0

for line in f:
    p, v, a = line.split()
    p = p.replace("p=<", "").strip(">,").split(",")
    p = [int(i) for i in p]
    v = v.replace("v=<", "").strip(">,").split(",")
    v = [int(i) for i in v]
    a = tuple(a.replace("a=<", "").strip(">,").split(","))
    a = [int(i) for i in a]

    parts[i] = Particle(p, v, a)
    i += 1

while True:
    for i, part in parts.items():
        part.step()

    pos_dict = defaultdict(list)
    for i, part in parts.items():
      k = tuple(part.p)
      pos_dict[k].append(i)

    for k, v in pos_dict.items():
      if len(v) > 1:
        for i in v:
          del parts[i]

    print(len(parts))

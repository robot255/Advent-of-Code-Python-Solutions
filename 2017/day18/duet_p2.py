from collections import defaultdict

f = open("input.txt", 'r')
instructions = [line.split() for line in f.read().strip().split("\n")]

r1 = defaultdict(int)
r2 = defaultdict(int)
r2['p'] = 1
ds = [r1, r2]


def get(s):
    if s in "qwertyuiopasdfghjklzxcvbnm":
        return d[s]
    return int(s)


tot = 0
ind = [0, 0]
snd = [[], []]
state = ["ok", "ok"]
pr = 0
d = ds[pr]
i = ind[0]

while True:
    instr = instructions[i]

    if instr[0] == "snd":
        if pr == 1:
            tot += 1
        snd[pr].append(get(instr[1]))
    elif instr[0] == "set":
        d[instr[1]] = get(instr[2])
    elif instr[0] == "add":
        d[instr[1]] += get(instr[2])
    elif instr[0] == "mul":
        d[instr[1]] *= get(instr[2])
    elif instr[0] == "mod":
        d[instr[1]] %= get(instr[2])
    elif instr[0] == "rcv":
        if snd[1-pr]:
            state[pr] = "ok"
            d[instr[1]] = snd[1 - pr].pop(0)
        else: # wait: switch to other prog
            if state[1-pr] == "done":
                break # will never recv: deadlock
            if len(snd[pr]) == 0 and state[1-pr] == "r":
                break # this one hasn't sent anything, other is recving: deadlock
            ind[pr] = i   # save instruction index
            state[pr] = "r" # save state
            pr = 1 - pr   # change program
            i = ind[pr] - 1 # (will be incremented back)
            d = ds[pr]    # change registers
    elif instr[0] == "jgz" and get(instr[1]) > 0:
        i += get(instructions[i][2]) - 1
    i += 1
    if not 0 <= i < len(instructions):
        if state[1-pr] == "done":
            break # both done
        state[pr] = "done"
        ind[pr] = i  # swap back since other program's not done
        pr = 1 - pr
        i = ind[pr]
        d = ds[pr]

print("solution: {0}".format(tot))
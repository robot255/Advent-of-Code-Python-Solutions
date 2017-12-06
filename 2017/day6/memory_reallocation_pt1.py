
def get_max_index(a):
    max = a[0]
    maxIndex = 0

    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
            maxIndex = i
    return max, maxIndex

def redistribute(memory):
    patterns = []

    redist = 0
    while str(memory) not in patterns:
        print("{0} {1}".format(memory, redist))
        patterns.append(str(memory))
        max_value, index = get_max_index(memory)

        memory[index] = 0

        for i in range(max_value):
            memory[(index + i + 1)%len(memory)] += 1

        redist +=1
    return redist

if __name__ == "__main__":
    f = open("input.txt", "r")
    lines = f.read().split()
    banks = [ int(i) for i in lines]
    #banks = [0,2,7,0]
    result = redistribute(banks)

    print("Solution: {0}".format(result))
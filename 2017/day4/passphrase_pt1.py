def passphrase(tokens):
    unique_tokens = set(tokens)
    return len(tokens) == len(unique_tokens)

if __name__ == "__main__":
    f = open("input.txt", "r")
    lines = f.readlines()

    total = 0
    for line in lines:
        if passphrase(line.split()):
            total += 1

    print("Solution: {0}".format(total))
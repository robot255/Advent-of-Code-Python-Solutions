def passphrase(tokens):
    unique_tokens = set(tokens)

    if len(tokens) != len(unique_tokens):
        return False

    sorted_tokens = [''.join(sorted(token)) for token in tokens]
    unique_sorted_tokens = set(sorted_tokens)

    return len(sorted_tokens) == len(unique_sorted_tokens)


if __name__ == "__main__":
    f = open("input.txt", "r")
    lines = f.readlines()

    total = 0
    for line in lines:
        if passphrase(line.split()):
            total += 1

    print("Solution: {0}".format(total))
def inverse_captcha(input):
    total = 0

    for idx, i in enumerate(input):
        if i == input[(idx + 1) % len(input)]:
            total += int(i)

    return total


if __name__ == '__main__':
    f = open("input.txt", "r")
    content = f.read()
    results = inverse_captcha(content)
    print("Solution: {0}".format(results))

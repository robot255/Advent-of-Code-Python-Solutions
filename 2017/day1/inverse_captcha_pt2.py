def inverse_captcha(input):
    total = 0
    for idx, digit in enumerate(input):
        forward_item = input[((idx) + len(input) // 2) % len(input)]
        if digit == forward_item:
            total += int(digit)

    return total

if __name__ == '__main__':
    f = open("input.txt", "r")
    content = f.read()
    results = inverse_captcha(content)
    print("Solution: {0}".format(results))

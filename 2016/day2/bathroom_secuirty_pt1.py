
keypad = {(-1, -1): 1, (0, -1): 2, (1, -1): 3,
          (-1, 0): 4, (0, 0): 5, (1, 0):6,
          (-1, 1): 7, (0, 1): 8, (1, 1): 9}

def keypad_locator(string):
    x = 0
    y = 0

    for i in string:
        if i == "U" and y != -1:
            y -= 1
        if i == "D" and y != 1:
            y += 1
        if i == "R" and x != 1:
            x += 1
        if i == "L" and x != -1:
            x -= 1

    return keypad[(x,y)]


if __name__ == "__main__":
    f = open("input.txt", "r")
    keypad_inputs = f.readlines()

    keycode = ""
    for keypad_input in keypad_inputs:
        keycode += str(keypad_locator(keypad_input))

    print("Solution: {0}".format(keycode))

keypad = {(0, 0): None, (1, 0): None, (2, 0):   1, (3, 0): None, (4, 0): None,
          (0, 1): None, (1, 1):    2, (2, 1):   3, (3, 1):    4, (4, 1): None,
          (0, 2):    5, (1, 2):    6, (2, 2):   7, (3, 2):    8, (4, 2):    9,
          (0, 3): None, (1, 3):  "A", (2, 3): "B", (3, 3):  "C", (4, 3): None,
          (0, 4): None, (1, 4): None, (2, 4): "D", (3, 4): None, (4, 4): None}

def keypad_locator(string):
    x = 0
    y = 2

    for i in string:
        if i == "U" and (x, y-1) in keypad and keypad[(x, y-1)]:
            y -= 1
        if i == "D" and (x, y+1) in keypad and keypad[(x, y+1)]:
            y += 1
        if i == "R" and (x+1, y) in keypad and keypad[(x+1, y)]:
            x += 1
        if i == "L" and (x-1, y) in keypad and keypad[(x-1, y)]:
            x -= 1

    return keypad[(x, y)]


if __name__ == "__main__":
    f = open("input.txt", "r")
    keypad_inputs = f.readlines()

    keycode = ""
    for keypad_input in keypad_inputs:
        keycode += str(keypad_locator(keypad_input))

    print("Solution: {0}".format(keycode))
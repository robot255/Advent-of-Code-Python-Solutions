
def is_nice(string):
    not_allowed_list = ["ab", "cd", "pq", "xy"]
    for not_allowed in not_allowed_list:
        if not_allowed in string:
            return False

    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    for vowel in vowels:
        vowel_count += string.count(vowel)

    if vowel_count < 3:
        return False

    for i in string:
        if i * 2 in string:
            return True

    return False

if __name__ == "__main__":
    f = open("input.txt", "r")
    strings = f.readlines()

    total_nice = 0
    for string in strings:
        if is_nice(string):
            total_nice += 1

    print("Solutions: {0}".format(total_nice))


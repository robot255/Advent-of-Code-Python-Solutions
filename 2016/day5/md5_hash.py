import hashlib

if __name__ == "__main__":
    santa_secret = "reyedfim"

    secret = 0
    while True:
        secret += 1
        m = hashlib.md5()
        m.update(santa_secret + str(secret))
        if m.hexdigest().startswith("00000"):
            break

    print("Solution: {0}".format(secret))

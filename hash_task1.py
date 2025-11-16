import sys
import hashlib


def check_hex(txt):
    for c in txt:
        if c not in "0123456789abcdefABCDEF":
            return False
    return True


def detect_type(h):

    h = h.strip()
    l = len(h)

    if not check_hex(h):
        return "Not valid hex"

    if l == 32:
        return "MD5"
    elif l == 40:
        return "SHA1"
    elif l == 64:
        return "SHA256"
    elif l == 96:
        return "SHA384"
    elif l == 128:
        return "SHA512"
    else:
        return "You have entered a wrong hash "


def make_md5(text):
    x = text.encode("utf-8")
    return hashlib.md5(x).hexdigest()


def menu():
    while True:
        print(" Hash Program ")
        print("1) Detect hash type")
        print("2) Generate MD5")
        print("3) Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            h = input("Enter hash: ")
            print("Type:", detect_type(h))

        elif ch == "2":
            t = input("Enter text: ")
            print("MD5:", make_md5(t))

        elif ch == "3":
            print("DONE")
            break

        else:
            print("Wrong choice , try again")


def main():

    if len(sys.argv) == 2:
        print(detect_type(sys.argv[1]))
    else:
        menu()

main()


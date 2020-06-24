
import cs50
import sys

def main():
    if len(sys.argv) != 2:
        print("You should provide a cmd line arguments!")
        exit(1)

    if sys.argv[1].isalpha() == False:
        print("You should provide valid keyword!")
        exit(1)

    pt = input("plaintext: ")
    conv = []
    keyIndex = 0
    keylength = len(sys.argv[1])

    for symbol in pt:
        if symbol.isalpha():
            key = ord(sys.argv[1][keyIndex % keylength].lower()) - 97
            keyIndex += 1
            if symbol.isupper():
                conv.append(chr(((ord(symbol) - 65 + key) % 26) + 65))
            else:
                conv.append(chr(((ord(symbol) - 97 + key) % 26) + 97))
        else:
            conv.append(symbol)

    print("ciphertext: " + "".join(conv))
    exit(0)


if __name__ == "__main__":
    main()
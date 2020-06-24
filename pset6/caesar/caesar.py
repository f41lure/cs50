
import cs50
import sys

def main():
    if len(sys.argv) != 2:
        print("You should provide cmd line arguments!")
        exit(1)
    key = int(sys.argv[1])
    phrase = input("Enter: ")

    list = phrase.split()
    newPhrase = ""
    for word in list:
        conversion = ''
        for ch in word:
            if ch.isalpha():
                if ch.islower():
                    conversion += (chr)((ord(ch) - ord("a") + key) % 26 + ord("a"))
                else:
                    conversion += (chr)((ord(ch) - ord("A") + key) % 26 + ord("A"))
            else:
                conversion += ch
        newPhrase = newPhrase + conversion + " "
    print("ciphertext: " + newPhrase.rstrip() + '\n')

if __name__ == "__main__":
    main()









string = input("string: ")
k = input("key: ")
j = 0
s = [x for x in string]
key = [f for f in k]

for i in range(0, len(s)):
    j = j % len(key)
    if s[i].isupper():
        if key[j].isupper():
            a = ord(key[j]) - 65
            b = ord(s[i]) - 65
            c = (a + b) % 26 + 65
            j += 1
            print(chr(c), end = '')


        if key[j].islower():
            a = ord(key[j]) - 97
            b = ord(s[i]) - 65
            c = (a + b) % 26 + 65
            j += 1
            print(chr(c), end = '')


    elif s[i].islower():
        if key[j].isupper():
            a = ord(key[j]) - 97
            b = ord(s[i]) - 65
            c = (a + b) % 26 + 97
            j += 1
            print(chr(c), end = '')


        if key[j].islower():
            a = ord(key[j]) - 97
            b = ord(s[i]) - 97
            c = (a + b) % 26 + 97
            j += 1
            print(chr(c), end = '')
    elif s[i].isalpha() != True:
        print(s[i], end = '')

print("\n")
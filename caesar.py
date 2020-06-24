while True:
    try:
        string = input("s");
        key = int(input("Key: "));
    except ValueError:
        print("<<<<RESTARTING>>>>");
        continue;
    else:
        break;
strlist = [x for x in string]
for i in range(0, len(string)):
    if strlist[i].isupper():
        a = ord(strlist[i])
        e = ((a - 65 + key) % 26) + 97
        c = chr(e)
        print(c.upper(), end = '')
    elif strlist[i].islower():
        a = ord(strlist[i])
        e = ((a - 97 + key) % 26) + 97
        c = chr(e)
        print(c, end = '')
    elif strlist[i].isalpha() != True:
        print(strlist[i], end = '')

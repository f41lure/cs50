from cs50 import *
# Mario.py
while True:

    length = get_int("Length:")

    if length > 23 or length <= 0:
        continue

    print('\n' * 24)

    for i in range(1, length + 1):
        space = ' '
        n = length - i
        print(space * n, end = '')
        print('#' * i, end = '')
        print(space * 2, end = '')
        print('#' * i)

    break


while True:
    try:
        change = float(input("Change: "))
    except ValueError:
        print("<<<<RESTARTING>>>>")
        continue
    else:
        break

while change < 0:
    change = float(input("Change: "))
change *= 100
coins = 0

while change != 0:
    if change >= 25:
        change -= 25
        coins += 1
    elif change >= 10  and change <= 25:
        change -= 10
        coins += 1
    elif change >= 5 and change <= 10:
        change -= 5
        coins += 1
    elif change >= 1 and change <= 5:
        change -= 1
        coins += 1
    if change == 0:
        break
print(coins)
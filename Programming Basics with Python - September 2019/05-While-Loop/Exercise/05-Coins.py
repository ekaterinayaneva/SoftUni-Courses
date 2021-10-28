import math

money = float(input())
money *= 100
money = math.floor(money)
counter = 0

while money > 0:
    if money / 200 >= 1:
        counter += 1
        money -= 200
    else:
        if money / 100 >= 1:
            counter += 1
            money -= 1

print(counter)

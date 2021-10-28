pastries = input()
number_of_pastries = int(input())
day = int(input())

price = 0

if pastries == "Cake":
    if day <= 15:
        price = 24
    if day > 15:
        price = 28.7
if pastries == "Souffle":
    if day <= 15:
        price = 6.66
    if day > 15:
        price = 9.8
if pastries == "Baklava":
    if day <= 15:
        price = 12.6
    if day > 15:
        price = 16.98

sum = number_of_pastries * price

if day <= 22:
    if sum > 200:
        sum = sum * 0.75

    elif 100 <= sum < 200:
        sum = sum * 0.85

if day <= 15:
    sum = sum * 0.9

print(f'{sum:.2f}')




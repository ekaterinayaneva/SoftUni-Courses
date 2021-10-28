a = int(input())

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0

for num in range(1, a+1):
    n = int(input())

    if n < 200:
        counter1 += 1
    if 200 <= n <= 399:
        counter2 += 1
    if 400 <= n <= 599:
        counter3 += 1
    if 600 <= n <= 799:
        counter4 += 1
    if n > 799:
        counter5 += 1

counter1 = (100 / a * counter1)
counter2 = (100 / a * counter2)
counter3 = (100 / a * counter3)
counter4 = (100 / a * counter4)
counter5 = (100 / a * counter5)

print(f'{counter1:.2f}%')
print(f'{counter2:.2f}%')
print(f'{counter3:.2f}%')
print(f'{counter4:.2f}%')
print(f'{counter5:.2f}%')

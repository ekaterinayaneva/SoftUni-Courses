n = int(input())

counter2 = 0
counter3 = 0
counter4 = 0

for nums in range(1, n+1):
    number = int(input())

    if number % 2 == 0:
        counter2 +=1
    if number % 3 == 0:
        counter3 += 1
    if number % 4 == 0:
        counter4 += 1

counter2 = (100 / n * counter2)
counter3 = (100 / n * counter3)
counter4 = (100 / n * counter4)

print(f'{counter2:.2f}%')
print(f'{counter3:.2f}%')
print(f'{counter4:.2f}%')


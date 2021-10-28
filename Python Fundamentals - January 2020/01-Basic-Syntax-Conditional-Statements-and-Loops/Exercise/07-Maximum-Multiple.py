divisor = int(input())
bound = int(input())

for x in range(bound, 0, -1):

    if x % divisor == 0:
        print(x)
        break

        
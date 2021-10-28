n = int(input())

for rows in reversed(str(n)):
    num = int(rows)
    for x in range(num):

        if num != 0:
            symbol = chr(num + 33)
            print(symbol, end='')
    if num == 0:
        print('ZERO')
    else:
        print()



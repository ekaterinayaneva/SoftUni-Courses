steps = str
all = 0

while all < 10000:
    steps = input()

    if steps == 'Going home':
        steps = input()
        all += int(steps)
        break

    all += int(steps)

if all < 10000:
    print(f'{10000 - all} more steps to reach goal.')
else:
    print('Goal reached! Good job!')

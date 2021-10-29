from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches = 0

while males and females:
    male = males[-1]
    female = females[0]

    if male <= 0:
        males.pop()

    elif female <= 0:
        females.popleft()

    elif male % 25 == 0:
        males.pop()
        if males:
            males.pop()

    elif female % 25 == 0:
        females.popleft()
        if females:
            females.popleft()

    elif male == female:
        males.pop()
        females.popleft()
        matches += 1

    else:
        females.popleft()
        males.append(males.pop() - 2)


print(f'Matches: {matches}')

print(f'Males left: {"none" if not males else ", ".join([str(x) for x in reversed(males)])}')
#print(f'Females left: {"none" if not females else ", ".join([str(x) for x in females])}')

if females:
    print(f'Females left: {", ".join([str(x) for x in females])}')
else:
    print(f'Females left: none')

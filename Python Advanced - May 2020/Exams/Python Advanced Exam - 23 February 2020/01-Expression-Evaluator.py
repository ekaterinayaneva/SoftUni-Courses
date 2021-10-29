from collections import deque
from math import floor

expression = deque(input().split())
saved_numbers = []

while True:

    current_el = expression.popleft()

    if current_el in '*+-/':
        result = floor(eval(current_el.join(saved_numbers)))       # floor, ot math.floor
        saved_numbers = []
        expression.appendleft(str(result))

        if len(expression) == 1:
            break

    else:
        saved_numbers.append(current_el)

print(expression[0])           # ako e samo expression ne stava

from collections import deque
from math import floor

expression = deque(input().split())
saved_numbers = []

while True:

    current_el = expression.popleft()

    if current_el in '*-+/':
        result = int(saved_numbers[0])

        for num in saved_numbers[1::]:

            if current_el == '+':
                result += int(num)
            elif current_el == '-':
                result -= int(num)
            elif current_el == '*':
                result *= int(num)
            elif current_el == '/':
                result /= int(num)

        saved_numbers = []
        expression.appendleft(str(floor(result)))

        if len(expression) == 1:
            break

    else:
        saved_numbers.append(current_el)

print(expression[0])

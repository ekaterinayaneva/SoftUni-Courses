N1 = int(input())
N2 = int(input())
operator = input()

even = str
odd = str

if operator == '+':
    result = N1 + N2
    if result % 2 == 0:
        even = 'even'
        print(f'{N1} {operator} {N2} = {result} - {even}')
    else:
        odd = 'odd'
        print(f'{N1} {operator} {N2} = {result} - {odd}')
elif operator == '-':
    result = N1 - N2
    if result % 2 == 0:
        even = 'even'
        print(f'{N1} {operator} {N2} = {result} - {even}')
    else:
        odd = 'odd'
        print(f'{N1} {operator} {N2} = {result} - {odd}')
elif operator == '*':
    result = N1 * N2
    if result % 2 == 0:
        even = 'even'
        print(f'{N1} {operator} {N2} = {result} - {even}')
    else:
        odd = 'odd'
        print(f'{N1} {operator} {N2} = {result} - {odd}')
elif operator == '/' and N2 != 0:
    result = N1 / N2
    print(f'{N1} {operator} {N2} = {result}')
elif operator == '/' and N2 == 0:
    print(f'Cannot divide {N1} by zero')
elif operator == '%' and N2 != 0:
    result = N1 % N2
    print(f'{N1} {operator} {N2} = {result}')
elif operator == '%' and N2 == 0:
    print(f'Cannot divide {N1} by zero')



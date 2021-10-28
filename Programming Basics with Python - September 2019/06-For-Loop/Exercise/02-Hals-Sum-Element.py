import sys
n = int(input())

max_number = -sys.maxsize
sum = 0

for nums in range(n):
    current_num = int(input())
    if current_num > max_number:
        max_number = current_num

    sum += current_num

sum -= max_number

if sum == max_number:
    print(f'Yes')
    print(f'Sum = {max_number}')
else:
    print(f'No')
    print(f'Diff = {abs(max_number-sum)}')

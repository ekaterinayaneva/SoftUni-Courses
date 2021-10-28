import sys

n = int(input())

sum = 0
current_sum = 0
max_sum = -sys.maxsize

for nums in range(n):
    num_1 = int(input())
    num_2 = int(input())

    sum = num_1 + num_2

    if sum != current_sum:
        max_sum = abs(sum - current_sum)

    current_sum = sum


if max_sum == current_sum:
    print(f"Yes, value={sum}")
else:
    print(f"No, maxdiff={max_sum}")




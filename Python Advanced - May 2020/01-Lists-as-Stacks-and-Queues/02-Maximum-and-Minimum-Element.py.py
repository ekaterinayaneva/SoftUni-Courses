import math
n = int(input())

stack_nums = []

for i in range(n):
    commands = input().split()
    command = int(commands[0])

    if command == 1:
        stack_nums.append(int(commands[1]))
    elif command == 2:
        if stack_nums:
            stack_nums.pop()
    elif command == 3:
        if stack_nums:
            print(max(stack_nums))
    elif command == 4:
        if stack_nums:
            print(min(stack_nums))

result = str(', '.join(map(str, reversed(stack_nums))))

print(result)              # ili           print(', '.join([str(x) for x in reversed(stack_nums)]))



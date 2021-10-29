clothes = list(input().split())
capacity = int(input())

sum_of_clothes = 0
rack = 1

clothes_stack = clothes[::-1]

while clothes_stack:
    current_cloth = clothes_stack.pop()

    sum_of_clothes += int(current_cloth)

    if sum_of_clothes > capacity:
        clothes_stack.append(current_cloth)
        sum_of_clothes = 0
        rack += 1

print(rack)



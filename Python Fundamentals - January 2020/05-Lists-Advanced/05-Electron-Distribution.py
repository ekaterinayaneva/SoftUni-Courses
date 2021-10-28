num = int(input())

result = []
counter = 1

while num > 0:
    add_num = 2 * counter ** 2

    if add_num > num:
        add_num = num
    result.append(add_num)
    num -= add_num
    counter += 1

print(result)



def is_palendrom(num_str):
    length = len(num_str)
    is_palendrom = True

    for i in range(length // 2):

        if num_str[i] != num_str[length - 1 - i]:
            is_palendrom = False
            break

    return is_palendrom


num_str = input().split(', ')

for num in num_str:
    print(is_palendrom(num))

# for i in num_str:
# number.append(int(i))
# length = len(number)
def is_palendrom(num_str):
    reversed_num = num_str[::-1]

    return True if reversed_num == num_str else False


num_str = input().split(', ')

for num in num_str:
    print(is_palendrom(num))

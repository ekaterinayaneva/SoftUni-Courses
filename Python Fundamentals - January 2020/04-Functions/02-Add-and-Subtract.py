def sum_numbers(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2, num_3):
    sum = sum_numbers(num_1, num_2)
    return sum - num_3


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(subtract(num_1, num_2, num_3))

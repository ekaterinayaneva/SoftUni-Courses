first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    even_sum = 0
    odd_sum = 0
    #number_to_str = str(number)

    for a, b in enumerate(str(number)):
        if a % 2 == 0:
            even_sum += int(b)
        else:
            odd_sum += int(b)

    if even_sum == odd_sum:
        print(number, end=' ')


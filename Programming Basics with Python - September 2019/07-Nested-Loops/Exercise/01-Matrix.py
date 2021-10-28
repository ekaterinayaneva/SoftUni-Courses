a = int(input())
b = int(input())
c = int(input())
d = int(input())

for first_row_first_number in range(a, b + 1):
    for first_row_second_number in range(a, b + 1):
        for second_row_first_number in range(c, d + 1):
            for second_row_second_number in range(c, d + 1):

                if first_row_first_number + second_row_second_number == first_row_second_number + second_row_first_number and \
                 first_row_first_number != first_row_second_number and second_row_first_number != second_row_second_number:

                    print(f'{first_row_first_number}{first_row_second_number}')
                    print(f'{second_row_first_number}{second_row_second_number}\n')


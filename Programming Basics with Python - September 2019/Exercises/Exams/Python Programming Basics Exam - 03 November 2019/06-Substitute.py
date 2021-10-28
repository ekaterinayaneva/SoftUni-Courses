k = int(input())
l = int(input())
m = int(input())
n = int(input())

counter = 0
has_ended = False

for first_first_num in range(k, 8):
    for second_first_num in range(9, l, -1):
        for first_second_num in range(m, 8):
            for second_second_num in range(9, n, -1):

                if first_first_num % 2 == 0 and first_second_num % 2 == 0 and second_first_num % 2 != 0 and second_second_num % 2 != 0:
                    if first_first_num + second_first_num == first_second_num + second_second_num:
                        print(f"Cannot change the same player.")
                    else:
                        print(f'{first_first_num}{second_first_num} - {first_second_num}{second_second_num}')
                        counter += 1

                    if counter >= 6:
                        break

            if has_ended:
                break
        if has_ended:
            break
    if has_ended:
        break



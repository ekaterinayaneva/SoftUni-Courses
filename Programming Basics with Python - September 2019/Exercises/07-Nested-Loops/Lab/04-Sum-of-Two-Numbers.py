first_num = int(input())
second_num = int(input())
magic_num = int(input())

counter = 0
is_found = False

for num1 in range(first_num, second_num + 1):
    for num2 in range(first_num, second_num + 1):

        counter += 1

        if num1 + num2 == magic_num:
            print(f"Combination N:{counter} ({num1} + {num2} = {magic_num})")
            is_found = True
            break
    if is_found :
        break

else:print(f"{counter} combinations - neither equals {magic_num}")





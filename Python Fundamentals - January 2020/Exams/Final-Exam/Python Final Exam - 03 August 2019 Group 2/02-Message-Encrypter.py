import re

n = int(input())

pattern = r"^([A-Za-z\s])*([\*|@])([A-Z][a-z]{2,})\2:\s\[([A-Z|a-z])\]\|\[([A-Z|a-z])\]\|\[([A-Z|a-z])\]\|$"


for num in range(n):
    message = input()

    match = re.match(pattern, message)

    if match is None:
        print(f"Valid message not found!")
        continue


    num_1 = ord(match[4])
    num_2 = ord(match[5])
    num_3 = ord(match[6])

    print(f'{match[3]}: {num_1} {num_2} {num_3}')


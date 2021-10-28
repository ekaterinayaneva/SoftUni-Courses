import re

n = int(input())

pattern  = r"(\$|%)([A-Z][a-z]{2,})\1:\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"

for num in range(n):
    message = input()

    match = re.match(pattern, message)

    if match is None:
        print('Valid message not found!')
        continue


    result = chr(int(match[3])) + chr(int(match[4])) + chr(int(match[5]))

    print(f'{match[2]}: {result}')


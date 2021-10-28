import re

n = int(input())

pattern = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]"

for num in range(n):
    message = input()

    match = re.match(pattern, message)

    if match is None:
        print(f"The message is invalid")
        continue

    encrypted_message = []                                  #ili encrypted_message = ''

    for ch in match[2]:
        encrypted_message.append(str(ord(ch)))                  #encrypted_message += str(ord(ch)) + ' '


    print(f'{match[1]}: {" ".join(encrypted_message)}')         #print(f'{match[1]}: {encrypted_message}')


phone_number = input().split('-')

phonebook = {}

while len(phone_number) != 1:
    name = phone_number[0]
    number = phone_number[1]
    phonebook[name] = number

    phone_number = input().split('-')

n = int(phone_number[0])

for _ in range(n):
    name = input()
    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')



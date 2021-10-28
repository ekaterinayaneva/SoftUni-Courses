import re

while True:
    command = input()

    if command == 'end':
        break


    pattern = r"^([A-Z]{1}[a-z\' ]+):([A-Z ]+)\b"

    match = re.match(pattern, command)

    if match is None:
        print(f'Invalid input!')
        continue

    encryption_key = len(command.split(':')[0])

    encryption_letter = []

    for ch in command:
        letter = ord(ch) + encryption_key

        if ch.isupper():
            if letter > 90:
                encryption_letter.append(chr(letter - 26))
            else:
                encryption_letter.append(chr(letter))

        elif ch.islower():
            if letter > 122:
                encryption_letter.append(chr(letter - 26))
            else:
                encryption_letter.append(chr(letter))

        elif ch.isspace():
            encryption_letter.append(' ')

        elif ch == "'":
            encryption_letter.append("'")

        elif ch == ':':
            encryption_letter.append('@')

    print(f"Successful encryption: {''.join(encryption_letter)}")






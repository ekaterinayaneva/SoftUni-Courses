message_input = input()

args = input()

while args != 'Reveal':
    args = args.split(':|:')
    command = args[0]

    if command == 'InsertSpace':
        index = int(args[1])
        message_input = message_input[0:index] + ' ' + message_input[index::]
        print(message_input)
    elif command == 'Reverse':
        substring = args[1]
        if substring in message_input:
            message_input = message_input.replace(substring, '', 1)
            reverse = substring[::-1]
            message_input = message_input[::] + reverse
            print(message_input)
        else:
            print(f'error')
    elif command == 'ChangeAll':
        substring = args[1]
        replacement = args[2]
        message_input = message_input.replace(substring, replacement)
        print(message_input)

    args = input()

print(f"You have a new text message: {message_input}")

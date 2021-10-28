password_input = input()

new_password = ''

args = input()

while args != 'Done':
    args = args.split()
    command = args[0]

    if command == 'TakeOdd':
        for ch in range(len(password_input)):
            if ch % 2 != 0:
                new_password += password_input[ch]
        print(new_password)

    elif command == 'Cut':
        index = int(args[1])
        length = int(args[2])

        new_password = new_password[0:index] + new_password[index + length::]
        print(new_password)

    elif command == 'Substitute':
        substring = args[1]
        substitute = args[2]

        if substring in new_password:
            new_password = new_password.replace(substring, substitute)
            print(new_password)
        else:
            print(f"Nothing to replace!")

    args = input()

if args == 'Done':
    print(f"Your password is: {new_password}")

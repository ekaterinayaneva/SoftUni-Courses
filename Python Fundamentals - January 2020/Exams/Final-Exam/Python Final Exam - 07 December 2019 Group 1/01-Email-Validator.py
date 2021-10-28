email = input()

args = input()

while args != 'Complete':

    command = args.split()

    if args == 'Make Upper':
        email = email.upper()
        print(email)

    elif args == 'Make Lower':
        email = email.lower()
        print(email)

    elif command[0] == 'GetDomain':
        count = int(command[1])
        print(email[-count:])

    elif args == 'GetUsername':
        index = email.find('@')
        if index == -1:
            print(f"The email {email} doesn't contain the @ symbol.")
        else:
            print(email[:index])

    elif command[0] == 'Replace':
        char = command[1]
        email = email.replace(char, '-')
        print(email)

    elif args == 'Encrypt':
        for ch in email:
            print(ord(ch), end=" ")


    args = input()


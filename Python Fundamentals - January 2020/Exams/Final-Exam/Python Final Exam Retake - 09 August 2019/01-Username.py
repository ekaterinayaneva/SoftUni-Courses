input_name = input()

args = input()

while args != "Sign up":
    command = args.split()[0]
    args = args.split()

    if command == 'Case':
        lower_upper = args[1]
        if lower_upper == 'lower':
            input_name = input_name.lower()
            #print(input_name)
        elif lower_upper == 'upper':
            input_name = input_name.upper()
        print(input_name)

    elif command == 'Reverse':
        start_index = int(args[1])
        end_index = int(args[2])
        if start_index <= -1 or end_index + 1 > len(input_name):
            args = input()
            continue
        reversed_str = input_name[end_index: start_index -1 :-1]
        print(reversed_str)

    elif command == 'Cut':
        substring = args[1]
        if substring in input_name:
            input_name = input_name.replace(substring, '')
            print(input_name)
        else:
            print(f"The word {input_name} doesn't contain {substring}.")

    elif command == 'Replace':
        char = args[1]
        input_name = input_name.replace(char, '*')
        print(input_name)
    elif command == 'Check':
        char = args[1]
        if char in input_name:
            print(f"Valid")
        else:
            print(f"Your username must contain {char}.")

    args = input()


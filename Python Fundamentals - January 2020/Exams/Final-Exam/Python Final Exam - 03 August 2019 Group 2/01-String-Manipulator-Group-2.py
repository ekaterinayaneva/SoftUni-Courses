string_input = input()

args = input()

while args != 'Done':
    args = args.split()
    command = args[0]

    if command == 'Change':
        char = args[1]
        replacement = args[2]
        string_input = string_input.replace(char, replacement)
        print(string_input)

    elif command == 'Includes':
        string = args[1]
        if string in string_input:
            print(f'True')
        else:
            print(f'False')
    elif command == 'End':
        string = args[1]
        result = string_input.endswith(string)
        print(result)
    elif command == 'Uppercase':
        string_input = string_input.upper()
        print(string_input)
    elif command == 'FindIndex':
        char = args[1]
        index = string_input.find(char)
        print(index)
    elif command == 'Cut':
        start_index = int(args[1])
        length = int(args[2])
        string_input = string_input[start_index: start_index + length]
        print(string_input)


    args = input()


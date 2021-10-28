string_input = input()

args = input().split()

while args[0] != 'End':
    command = args[0]

    if command == 'Translate':
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
    elif command == 'Start':
        string = args[1]
        result = string_input.startswith(string)
        print(result)
    elif command == 'Lowercase':
        string_input = string_input.lower()
        print(string_input)
    elif command == 'FindIndex':
        char = args[1]
        index = string_input.rindex(char)
        print(index)
    elif command == 'Remove':
        start_index = int(args[1])
        count = int(args[2])
        string_input = string_input[0: start_index] + string_input[start_index + count:]
        print(string_input)

    args = input().split()

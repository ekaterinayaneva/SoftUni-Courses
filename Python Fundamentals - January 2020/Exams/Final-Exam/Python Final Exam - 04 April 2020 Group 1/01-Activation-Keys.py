string_input = input()

while True:
    args = input().split('>>>')
    command = args[0]

    if command == 'Generate':
        print(f"Your activation key is: {string_input}")
        break

    elif command == 'Contains':
        substring = args[1]
        if substring in string_input:
            print(f"{string_input} contains {substring}")
        else:
            print(f"Substring not found!")

    elif command == 'Flip':
        upper_lower = (args[1].split('/'))
        upper_lower = ''.join(upper_lower)
        start_index = int(args[2])
        end_index = int(args[3])

        if upper_lower == 'Upper':
            string_input = string_input[0:start_index] + string_input[start_index:end_index].upper() + string_input[end_index::]
        elif upper_lower == 'Lower':
            string_input = string_input[0:start_index] + string_input[start_index:end_index].lower() + string_input[
                                                                                                       end_index::]
        print(string_input)
    elif command == 'Slice':
        start_index = int(args[1])
        end_index = int(args[2])
        string_input = string_input[0:start_index] + string_input[end_index::]

        print(string_input)

        
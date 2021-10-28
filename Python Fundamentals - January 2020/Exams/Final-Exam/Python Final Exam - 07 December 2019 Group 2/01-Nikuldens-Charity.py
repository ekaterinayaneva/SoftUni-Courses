text_input = input()

args = input().split()
total_sum = 0

while args[0] != "Finish":
    command = args[0]

    if command == 'Replace':
        current_char = args[1]
        new_char = args[2]
        text_input = text_input.replace(current_char, new_char)
        print(text_input)
    elif command == 'Cut':
        start_index = int(args[1])
        end_index = int(args[2])
        if end_index + 1 > len(text_input):
            print(f"Invalid indexes!")
        else:
            text_input = text_input[0: start_index] + text_input[end_index+1::]
            print(text_input)
    elif command == 'Make':
        upper_lower = args[1]
        if upper_lower == 'Upper':
            text_input = text_input.upper()
            print(text_input)
        elif upper_lower == 'Lower':
            text_input = text_input.lower()
            print(text_input)
    elif command == 'Check':
        string = args[1]
        if string in text_input:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")
    elif command == 'Sum':
        start_index = int(args[1])
        end_index = int(args[2])
        if start_index <= -1 or end_index + 1 > len(text_input):
            print(f"Invalid indexes!")
        else:
            sum_of_indexes = text_input[start_index:end_index+1]
            for index in sum_of_indexes:
                total_sum += (ord(index))
            print(total_sum)

    args = input().split()


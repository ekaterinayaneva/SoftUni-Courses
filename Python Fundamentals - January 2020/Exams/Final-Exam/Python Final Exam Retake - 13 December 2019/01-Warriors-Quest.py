string_input = input()

args = input()

while args != "For Azeroth":
    command = args.split()[0]
    args = args.split()

    # if command == "For Azeroth":
    #    break

    if command == "GladiatorStance":
        string_input = string_input.upper()
        print(string_input)
    elif command == "DefensiveStance":
        string_input = string_input.lower()
        print(string_input)
    elif command == "Dispel":
        index = int(args[1])
        letter = args[2]
        if index + 1 <= len(string_input):
            string_input = list(string_input)
            string_input[index] = letter
            string_input = ''.join(string_input)
            print(f"Success!")
        else:
            print(f"Dispel too weak.")
    elif args[1] == "Change":
        substring = args[2]
        second_substring = args[3]
        string_input = string_input.replace(substring, second_substring)
        print(string_input)
    elif args[1] == "Remove":
        substring = args[2]
        string_input = string_input.replace(substring, '')
        print(string_input)
    else:
        print(f"Command doesn't exist!")

    args = input()


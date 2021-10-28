username = input()

while True:
    command = input()
    if command == "Sign up":
        break
    tokens = command.split()
    action = tokens[0]

    if action == "Case":
        subaction = tokens[1]
        if subaction == "lower":
            username = username.lower()
        elif subaction == "upper":
            username = username.upper()
        print(username)

    elif action == "Reverse":
        start = int(tokens[1])
        end = int(tokens[2])
        if start not in range(len(username)) or end not in range(len(username)):
            continue
        rev_user = username[start:end + 1]
        rev_user = rev_user[::-1]
        print(rev_user)

    elif action == "Cut":
        substring = tokens[1]
        if substring not in username:
            print(f"The word {username} doesn't contain {substring}.")
            continue
        username = username.replace(substring, "")
        print(username)

    elif action == "Replace":
        char = tokens[1]
        if char not in username:
            continue
        username = username.replace(char, "*")
        print(username)

    elif action == "Check":
        char = tokens[1]
        if char not in username:
            print(f"Your username must contain {char}.")
        else:
            print("Valid")



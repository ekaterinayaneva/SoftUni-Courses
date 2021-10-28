usernames = input().split(', ')

instructions = input().split(' ')
blacklisted_count = 0
lost_count = 0

while instructions[0] != 'Report':
    command = instructions[0]

    if command == 'Blacklist':
        new_name = instructions[1]
        if new_name in usernames:
            index = usernames.index(new_name)
            usernames[index] = 'Blacklisted'
            blacklisted_count += 1
            print(f"{new_name} was blacklisted.")
        else:
            print(f"{new_name} was not found.")
    elif command == 'Error':
        index = int(instructions[1])
        if usernames[index] != 'Blacklisted' or usernames[index] != 'Lost':
            usernames[index] = 'Lost'
            lost_count += 1
            print(f"{usernames[index]} was lost due to an error.")
    elif command == 'Change':
        index = int(instructions[1])
        new_name = instructions[2]
        if 0 <= index < len(usernames):
            name = usernames[index]
            usernames[index] = new_name
            print(f"{name} changed his username to {new_name}.")

print(' '.join(usernames))

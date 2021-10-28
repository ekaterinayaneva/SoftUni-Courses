usernames = input().split(', ')

while True:
    command = input().split()
    if command[0] == 'Report':
        break
    if command[0] == 'Blacklist':
        if command[1] in usernames:
            for i in range(len(usernames)):
                if command[1] == usernames[i]:
                    usernames[i] = 'Blacklisted'
                    print(f'{command[1]} was blacklisted.')
                    break
        else:
            print(f'{command[1]} was not found.')
    elif command[0] == 'Error':
        str = ''
        index = int(command[1])
        if 0 <= index <= len(usernames) - 1:
            if usernames[index] == 'Blacklisted' or usernames[index] == 'Lost':
                continue
            else:
                str = usernames[index]
                usernames[index] = 'Lost'
                print(f'{str} was lost due to an error.')
    elif command[0] == 'Change':
        index = int(command[1])
        if 0 <= index <= len(usernames) - 1:
            print(f'{usernames[index]} changed his username to {command[2]}.')
            usernames[index] = command[2]

            
print(f"Blacklisted names: {usernames.count('Blacklisted')}")
print(f"Lost names: {usernames.count('Lost')}")
print(*usernames, sep=' ')

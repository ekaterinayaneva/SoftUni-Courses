followers = {}
command = input()

while command != 'Log out':
    command_list = command.split(": ")

    if command_list[0] == 'New follower':
        user = command_list[1]
        if user not in followers:
            followers[user] = [0, 0]

    elif command_list[0] == 'Like':
        user = command_list[1]
        count = int(command_list[2])

        if user not in followers:
            followers[user] = [0, 0]

        followers[user][0] += count

    elif command_list[0] == 'Comment':
        user = command_list[1]
        count = 1

        if user not in followers:
            followers[user] = [0, 0]

        followers[user][1] += count

    elif command_list[0] == 'Blocked':
        user = command_list[1]

        if user in followers:
            del followers[user]
        else:
            print(f"{user} doesn't exist.")

    command = input()

sorted_followers = dict(sorted(followers.items()))
sorted_followers = dict(sorted(sorted_followers.items(), key=lambda x: x[1][0], reverse=True))

print(f'{len(followers)} followers')

for k, v in sorted_followers.items():
    print(f'{k}: {sum(v)}')
args = input().split(':')

records = {}

while True:
    command = args[0]

    if command == 'Log out':
        break

    if command == 'New follower':
        username = args[1]
        if username not in records:
            records[username] = []

    elif command == 'Like':
        username = args[1]
        count = int(args[2])

        if username not in records:
            records[username] = [count]
            args = input().split(':')
            continue

        records[username].append(count)

    elif command == 'Comment':
        username = args[1]

        if username not in records:
            records[username] = [1]
            args = input().split(':')
            continue

        records[username].append(1)

    elif command == 'Blocked':
        username = args[1]

        if username not in records:
            print(f"{username} doesn't exist.")
            args = input().split(':')
            continue

        del records[username]

    args = input().split(':')


for username, value in records.items():
    records[username] = sum(value)


records = dict(sorted(records.items(), key=lambda v: (-(v[1]), v[0])))

print(f'{len(records)} followers')

for username, value in records.items():
    print(f'{username.lstrip()}: {value}')


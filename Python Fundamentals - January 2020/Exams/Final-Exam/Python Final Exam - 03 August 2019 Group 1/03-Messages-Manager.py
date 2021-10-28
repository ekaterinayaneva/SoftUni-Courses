messages_capacity = int(input())

args = input().split('=')

records = {}

while args[0] != 'Statistics':
    command = args[0]

    if command == 'Add':
        username = args[1]
        sent = int(args[2])
        received = int(args[3])
        if username in records:
            args = input().split('=')
            continue

        records[username] = []
        records[username].append(sent)
        records[username].append(received)

    elif command == 'Message':
        sender = args[1]
        receiver = args[2]
        if sender in records and receiver in records:

            records[sender][0] += 1
            if records[sender][0] + records[sender][1] >= messages_capacity:
                del records[sender]
                print(f"{sender} reached the capacity!")

            records[receiver][1] += 1

            if records[receiver][1] + records[receiver][0] >= messages_capacity:
                del records[receiver]
                print(f"{receiver} reached the capacity!")

    elif command == 'Empty':
        username = args[1]

        if username == 'All':
            records = {}
        else:
            del records[username]


    args = input().split('=')


print(f'Users count: {len(records)}')


for username, messages in sorted(records.items(), key=lambda m: (-m[1][1], m[0])):
    print(f'{username} - {sum(messages)}')



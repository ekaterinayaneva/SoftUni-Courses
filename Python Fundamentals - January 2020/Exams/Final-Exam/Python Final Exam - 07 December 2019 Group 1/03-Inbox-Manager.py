text_input = input().split('->')
users_list = {}

while text_input[0] != "Statistics":
    command = text_input[0]
    username = text_input[1]

    if command == 'Add':
        if username in users_list:
            print(f"{username} is already registered")
        else:
            users_list[username] = []
    elif command == 'Send':
        email = text_input[2]
        users_list[username].append(email)
    elif command == 'Delete':
        if username in users_list:
            users_list.pop(username)
        else:
            print(f"{username} not found!")

    text_input = input().split('->')

users_list = dict(sorted(users_list.items(), key=lambda v: (-len(v[1]), v[0])))

print(f"Users count: {len(users_list)}")

for user, emails in users_list.items():
    print(user)
    for email in emails:
        print(f' - {email}')

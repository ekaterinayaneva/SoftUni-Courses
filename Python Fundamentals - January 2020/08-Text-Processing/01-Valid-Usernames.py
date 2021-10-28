usernames = input().split(', ')

for username in usernames:

    if not 3 <= len(username) <= 16:
        continue

    is_valid = True

    for ch in username:
        if not (ch.isalnum() or ch == '_' or ch == '-'):
            is_valid = False
            break

    if not is_valid:
        continue

    print(username)



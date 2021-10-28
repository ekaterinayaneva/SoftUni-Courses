def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


numbers = int(input())

registered_users = {}

for i in range(1, numbers + 1):
    instructions = input().split()
    command = instructions[0]

    if command == 'register':
        name = instructions[1]
        license_plate_number = instructions[2]
        if name not in registered_users:
            print(f"{name} registered {license_plate_number} successfully")
            validate_key_existing(registered_users, name)
            registered_users[name] = license_plate_number
        else:
            print(f"ERROR: already registered with plate number {registered_users[name]}")

    elif command == 'unregister':
        name = instructions[1]
        if name in registered_users:
            registered_users.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for k, v in registered_users.items():
    print(f'{k} => {v}')

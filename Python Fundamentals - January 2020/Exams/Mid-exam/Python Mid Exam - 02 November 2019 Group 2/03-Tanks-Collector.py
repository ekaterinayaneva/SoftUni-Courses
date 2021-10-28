owned_tanks = input().split(', ')
commands = int(input())

for i in range(1, commands+1):
    instruction = input().split(', ')
    command = instruction[0]

    if command == 'Add':
        tank_name = instruction[1]
        if tank_name in owned_tanks:
            print(f"Tank is already bought")
        else:
            owned_tanks.append(tank_name)
            print(f"Tank successfully bought" )
    elif command == 'Remove':
        tank_name = instruction[1]
        if tank_name in owned_tanks:
            owned_tanks.remove(tank_name)
            print(f"Tank successfully sold" )
        else:
            print(f"Tank not found")
    elif command == 'Remove At':
        index = int(instruction[1])
        if 0 <= index < len(owned_tanks):
            owned_tanks.pop(index)
            print(f"Tank successfully sold")
        else:
            print(f"Index out of range" )
    elif command == 'Insert':
        index = int(instruction[1])
        tank_name = instruction[2]
        if 0 <= index < len(owned_tanks):
            if tank_name in owned_tanks:
                print(f"Tank is already bought")
            elif tank_name not in owned_tanks:
                owned_tanks.insert(index, tank_name)
                print(f"Tank successfully bought")
        else:
            print(f"Index out of range")

print(', '.join(owned_tanks))


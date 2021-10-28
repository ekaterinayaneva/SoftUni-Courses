pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health = int(input())

game_over = False

instructions = input().split()
while instructions[0] != 'Retire':
    command = instructions[0]

    if command == 'Fire':
        index = int(instructions[1])
        damage = int(instructions[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                game_over = True
                break
    elif command == 'Defend':
        start_index = int(instructions[1])
        end_index = int(instructions[2])
        damage = int(instructions[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    game_over = True
                    break
    elif command == 'Repair':
        index = int(instructions[1])
        health = int(instructions[2])
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health
    elif command == 'Status':
        counter = 0
        for sector in pirate_ship:
            if sector < max_health * 0.2:
                counter += 1
        print(f"{counter} sections need repair.")

    instructions = input().split()

if not game_over:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")





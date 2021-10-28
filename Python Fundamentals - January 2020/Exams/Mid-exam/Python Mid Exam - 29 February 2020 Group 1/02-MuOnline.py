string_input = input().split('|')

health = 100
bitcoins = 0
rooms = 0

for x in string_input:
    command = x.split()
    rooms += 1

    if command[0] == 'potion':
        health_plus = int(command[1])

        healed = 100 - health

        if health < 100:
            health += health_plus
            if health >= 100:
                health = 100
                print(f"You healed for {healed} hp.")
            else:
                print(f"You healed for {health_plus} hp.")
        print(f"Current health: {health} hp.")

    elif command[0] == 'chest':
        bits = int(command[1])
        bitcoins += bits
        print(f"You found {bits} bitcoins.")

    else:
        monster = command[0]
        attack = int(command[1])

        health -= attack
        if health > 0:
            print(f"You slayed {monster}.")
        elif health <= 0:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {rooms}")
            break

if rooms == len(string_input) and health > 0:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")



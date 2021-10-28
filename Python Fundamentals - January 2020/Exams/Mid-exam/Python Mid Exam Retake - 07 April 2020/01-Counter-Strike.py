initial_energy = int(input())

args = input()

won_battles = 0

while args != 'End of battle':
    energy = int(args)

    if initial_energy < energy:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
        break

    initial_energy -= energy

    won_battles += 1

    if won_battles % 3 == 0:
        initial_energy += won_battles


    args = (input())

if args == 'End of battle':
    print(f"Won battles: {won_battles}. Energy left: {initial_energy}")


budget = int(input())

command = input()
while command != 'Stop':
    item_price = 0

    for char in command:
        item_price += ord(char)

    if item_price <= budget:
        budget -= item_price
        print(f"Item successfully purchased!")
    else:
        print(f"Not enough money!")
        break

    command = input()

if command == 'Stop':
    print(f"Money left: {budget}")


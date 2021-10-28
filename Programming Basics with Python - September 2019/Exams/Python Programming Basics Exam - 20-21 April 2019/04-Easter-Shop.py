quantity_egg = int(input())

sold_eggs = 0

command = input()
while command != 'Close':
    eggs_number = int(input())

    if command == 'Fill':
        quantity_egg += eggs_number

    if quantity_egg < eggs_number:
        print(f"Not enough eggs in store!")
        print(f"You can buy only {quantity_egg}.")
        break

    if command == 'Buy':
        quantity_egg -= eggs_number
        sold_eggs += eggs_number

    command = input()

if command == 'Close':
    print(f"Store is closed!")
    print(f"{sold_eggs} eggs sold.")



coffee_quantity = int(input())

day_earnings = 0
price = 0
needed_coffee = 0

command = input()
while command != 'closed':

    if command == 'espresso':
        price = 3
        needed_coffee = 50
    elif command == 'cappuccino':
        price = 3.5
        needed_coffee = 30
    elif command == 'latte':
        price = 3.5
        needed_coffee = 20

    if coffee_quantity > needed_coffee:
        coffee_quantity -= needed_coffee
        day_earnings += price

    elif coffee_quantity == needed_coffee:
        day_earnings += price
        print(f'No more coffee left!')
        print(f'Profit: {day_earnings:.2f} lv.')
        break

    elif coffee_quantity < needed_coffee:
        print(f'Not enough coffee!')


    command = input()
if command == 'closed':
    print(f'Coffee left: {coffee_quantity}g')
    print(f'Profit: {day_earnings:.2f} lv.')



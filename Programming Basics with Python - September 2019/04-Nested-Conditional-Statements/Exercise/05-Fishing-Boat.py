budget = int(input())
season = input()
fishermen = int(input())

boat_price = 0
discount = 0
if season == 'Spring':
    boat_price = 3000
    if fishermen <= 6:
        discount = 0.1
    elif 7 <= fishermen <= 11:
        discount = 0.15
    elif fishermen >= 12:
        discount = 0.25
elif season == 'Summer':
    boat_price = 4200
    if fishermen <= 6:
        discount = 0.1
    elif 7 <= fishermen <= 11:
        discount = 0.15
    elif fishermen >= 12:
        discount = 0.25
elif season == 'Autumn':
    boat_price = 4200
    if fishermen <= 6:
        discount = 0.1
    elif 7 <= fishermen <= 11:
        discount = 0.15
    elif fishermen >= 12:
        discount = 0.25
elif season == 'Winter':
    boat_price = 2600
    if fishermen <= 6:
        discount = 0.1
    elif 7 <= fishermen <= 11:
        discount = 0.15
    elif fishermen >= 12:
        discount = 0.25

boat_price -= boat_price * discount

if fishermen %2 == 0 and season != 'Autumn':
    boat_price = boat_price * 0.95

if budget >= boat_price:
    left_money = budget - boat_price
    print(f'Yes! You have {left_money:.2f} leva left.')
elif budget < boat_price:
    needed_money = abs(budget - boat_price)
    print(f'Not enough money! You need {needed_money:.2f} leva.')



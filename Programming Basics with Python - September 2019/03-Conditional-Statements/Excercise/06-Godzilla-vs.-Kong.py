film_budget = float(input())
supernumeraries = int(input())
clothing_price = float(input())

decor_price = film_budget * 0.1

clothing_price = clothing_price * supernumeraries

if supernumeraries > 150:
    clothing_price *= 0.9


needed_money_for_filming = decor_price + clothing_price


if needed_money_for_filming > film_budget:
    print('Not enough money!')
    left_money = needed_money_for_filming - film_budget
    print(f'Wingard needs {left_money:.2f} leva more.')
else:
    print('Action!')
    left_money = film_budget - needed_money_for_filming
    print(f'Wingard starts filming with {left_money:.2f} leva left.')





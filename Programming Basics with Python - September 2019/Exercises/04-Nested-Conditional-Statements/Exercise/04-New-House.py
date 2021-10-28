flower_type = input()
number_of_flowers = int(input())
budget = int(input())

price = 0
discount = 0

if flower_type == 'Roses':
    price = 5
    if number_of_flowers > 80:
        discount = 0.1
elif flower_type == 'Dahlias':
    price = 3.8
    if number_of_flowers > 90:
        discount = 0.15
elif flower_type == 'Tulips':
    price = 2.8
    if number_of_flowers > 80:
        discount = 0.15
elif flower_type == 'Narcissus':
    price = 3
    if number_of_flowers < 120:
        price = price * 1.15
elif flower_type == 'Gladiolus':
    price = 2.5
    if number_of_flowers < 80:
        price = price * 1.2

project_garden = number_of_flowers * price
project_garden -= project_garden * discount

if project_garden <= budget:
    rest_money = budget - project_garden
    print(f'Hey, you have a great garden with {number_of_flowers} {flower_type} and {rest_money:.2f} leva left.')
elif project_garden > budget:
    needed_money = abs(budget - project_garden)
    print(f'Not enough money, you need {needed_money:.2f} leva more.')



import math
sushi_type = input()
restaurant_name = input()
number_of_servings = int(input())
order = input()

sushi_price = 0

if sushi_type == 'sashimi':
    if restaurant_name == 'Sushi Zone':
        sushi_price = 4.99
    if restaurant_name == 'Sushi Time':
        sushi_price = 5.49
    if restaurant_name == 'Sushi Bar':
        sushi_price = 5.25
    if restaurant_name == 'Asian Pub':
        sushi_price = 4.5
if sushi_type == 'maki':
    if restaurant_name == 'Sushi Zone':
        sushi_price = 5.29
    if restaurant_name == 'Sushi Time':
        sushi_price = 4.69
    if restaurant_name == 'Sushi Bar':
        sushi_price = 5.55
    if restaurant_name == 'Asian Pub':
        sushi_price = 4.8
if sushi_type == 'uramaki':
    if restaurant_name == 'Sushi Zone':
        sushi_price = 5.99
    if restaurant_name == 'Sushi Time':
        sushi_price = 4.49
    if restaurant_name == 'Sushi Bar':
        sushi_price = 6.25
    if restaurant_name == 'Asian Pub':
        sushi_price = 5.5
if sushi_type == 'temaki':
    if restaurant_name == 'Sushi Zone':
        sushi_price = 4.29
    if restaurant_name == 'Sushi Time':
        sushi_price = 5.19
    if restaurant_name == 'Sushi Bar':
        sushi_price = 4.75
    if restaurant_name == 'Asian Pub':
        sushi_price = 5.5

order_price = number_of_servings * sushi_price

if restaurant_name != "Sushi Zone"\
        and restaurant_name != "Sushi Time" \
        and restaurant_name != "Sushi Bar" \
        and restaurant_name != "Asian Pub":
    print(f'{restaurant_name} is invalid restaurant!')

if order == 'N':
    if restaurant_name == "Sushi Zone" \
        or restaurant_name == "Sushi Time" \
        or restaurant_name == "Sushi Bar" \
        or restaurant_name == "Asian Pub":
        order_price = math.ceil(order_price)
        print(f'Total price: {order_price} lv.')
elif order == 'Y':
    if restaurant_name == "Sushi Zone" \
            or restaurant_name == "Sushi Time" \
            or restaurant_name == "Sushi Bar" \
            or restaurant_name == "Asian Pub":
        plus_20 = order_price * 1.2
        plus_20 = math.ceil(plus_20)
        print(f'Total price: {plus_20} lv.')



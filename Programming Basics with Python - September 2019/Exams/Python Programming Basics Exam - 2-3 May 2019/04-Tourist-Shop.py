budget = float(input())

counter_product = 0
total_price = 0

product_name = input()
while product_name != 'Stop':

    counter_product += 1

    product_price = float(input())

    if counter_product % 3 == 0:
        product_price = product_price * 0.5

    total_price += product_price

    if budget < product_price:
        print(f"You don't have enough money!")
        print(f"You need {product_price - budget:.2f} leva!")
        break

    budget -= product_price

    product_name = input()

if product_name == 'Stop':
    print(f"You bought {counter_product} products for {total_price:.2f} leva.")


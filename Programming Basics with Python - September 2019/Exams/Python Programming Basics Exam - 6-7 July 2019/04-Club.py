club_profit = float(input())

length = 0
price = 0
profit_reaching = 0

while True:
    cocktail_name = input()

    if cocktail_name == 'Party!':
        print(f"We need {club_profit - profit_reaching:.2f} leva more.")
        print(f"Club income - {profit_reaching:.2f} leva.")
        break

    number_of_cocktails = int(input())

    length = len(cocktail_name)
    price = length * 1 * number_of_cocktails

    if price % 2 == 1:
        price = price * 0.75

    profit_reaching += price

    if profit_reaching >= club_profit:
        print(f"Target acquired.")
        print(f"Club income - {profit_reaching:.2f} leva.")
        break



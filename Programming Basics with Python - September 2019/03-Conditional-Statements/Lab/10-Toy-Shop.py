excursion_price = float(input())
puzzles = int(input())
speaking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
tracks = int(input())

collected_money = puzzles * 2.6 + speaking_dolls * 3 + teddy_bears * 4.1 + minions * 8.2 + tracks * 2

toys_count = puzzles + speaking_dolls + teddy_bears + minions + tracks

if toys_count >= 50:
    percentage_sale = collected_money * 0.25
else: percentage_sale = 0


end_price = collected_money - percentage_sale

rent = end_price * 0.1

earnings = end_price - rent

profit = earnings - excursion_price

if profit >= excursion_price:
    print(f' Yes! {profit:.2f} lv left.')
else: print(f' Not enough money! {abs(profit):.2f} lv needed.')





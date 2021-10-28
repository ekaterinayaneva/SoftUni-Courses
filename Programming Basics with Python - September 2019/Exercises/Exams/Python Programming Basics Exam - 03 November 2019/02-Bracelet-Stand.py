pockets_day_money = float(input())
earned_day_money = float(input())
coast = float(input())
gift_price = float(input())

pockets_money = 5 * pockets_day_money
earned_money = 5 * earned_day_money

collected_money = pockets_money + earned_money - coast

if collected_money > gift_price:
    print(f"Profit: {collected_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {gift_price - collected_money:.2f} BGN.")




baklava_price = float(input())
muffins_price = float(input())
schtolen_kilo = float(input())
candy_kilo = float(input())
biscuits_kilo = int(input())

schtolen_price = baklava_price + baklava_price * 0.6
schtolen_end_price = schtolen_price * schtolen_kilo

candy_price = muffins_price + muffins_price * 0.8
candy_end_price = candy_price * candy_kilo

biscuits_end_price = biscuits_kilo * 7.5

needed_money = schtolen_end_price + candy_end_price + biscuits_end_price

print(f'{needed_money:.2f}')




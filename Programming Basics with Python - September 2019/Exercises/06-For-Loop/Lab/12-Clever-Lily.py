Lilys_age = int(input())
washing_machine = float(input())
toys_price = int(input())

toys_count = 0
money_to_receive = 0
saved_money = 0

for year in range(1, Lilys_age+1):
    if year % 2 != 0:
        toys_count += 1
    else:
        money_to_receive += 10
        saved_money += money_to_receive
        saved_money -= 1

saved_money += toys_count * toys_price

if saved_money < washing_machine:
    difference = washing_machine - saved_money
    print(f'No! {difference:.2f}')
else:
    difference = saved_money - washing_machine
    print(f'Yes! {difference:.2f}')


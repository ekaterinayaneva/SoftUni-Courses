needed_money = float(input())
months = int(input())

collected_money = 0

for month in range(1, months+1):

    if month % 2 != 0:
        if month != 1:
            collected_money *= 0.84

    if month % 4 == 0:
        collected_money *= 1.25

    collected_money += needed_money * 0.25

if collected_money > needed_money:
    print(f"Bravo! You can go to Disneyland and you will have {collected_money - needed_money:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {needed_money - collected_money:.2f}lv. more.")


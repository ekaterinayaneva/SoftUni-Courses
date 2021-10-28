import math

needed_money = float(input())
fantasy_books = int(input())
horror_books = int(input())
romantic_books = int(input())

sum_of_saled_books = fantasy_books * 14.9 + horror_books * 9.8 + romantic_books * 4.3
dds_sum = sum_of_saled_books * 0.8

if dds_sum > needed_money:
    sellers_remuneration = dds_sum - needed_money
    sellers_remuneration = sellers_remuneration * 0.1
    sellers_remuneration = math.floor(sellers_remuneration)

    total_donated_sum = dds_sum - needed_money - sellers_remuneration
    total_donated_sum = total_donated_sum + needed_money

if dds_sum > needed_money:
    print(f'{total_donated_sum:.2f} leva donated.')
    print(f"Sellers will receive {sellers_remuneration} leva.")
else:
    need = needed_money - dds_sum
    print(f"{need:.2f} money needed.")







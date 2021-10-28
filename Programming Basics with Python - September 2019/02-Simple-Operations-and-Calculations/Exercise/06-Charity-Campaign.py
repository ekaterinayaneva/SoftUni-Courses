days = int(input())
pastry_cookers = int(input())
cakes = int(input())
waffels = int(input())
pancakes = int(input())

cakes_sum = cakes * 45
waffels_sum = waffels * 5.8
pancakes_sum = pancakes * 3.2

sum_per_day = (cakes_sum + waffels_sum + pancakes_sum) * pastry_cookers

campaign_sum = sum_per_day * days

ingredients_coasts = campaign_sum - (1/8 * campaign_sum)

collected_money = ingredients_coasts

print(f'{collected_money:.2f}')

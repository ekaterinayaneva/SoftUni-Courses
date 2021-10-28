quantity = int(input())   #3
days = int(input())   #20

ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15

spirit = 0
costs = 0

for day in range(1, days +1):

    if day % 2 == 0:
        costs += quantity * ornament_set_price
        spirit += 5

    if day % 3 == 0:
        costs += quantity * (tree_skirt_price + tree_garlands_price)
        spirit += 13

    if day % 5 == 0:
        costs += quantity * tree_lights_price
        spirit += 17

    if day % 15 == 0:
        spirit += 30
        costs += quantity * (tree_skirt_price + tree_garlands_price + tree_lights_price)

    if day % 10 == 0:
        spirit -= 20
        costs += tree_skirt_price + tree_garlands_price + tree_lights_price
        if day == days:
            spirit -= 30

    if day % 11 == 0:
        quantity += 2


print(f'Total cost: {costs}')
print(f"Total spirit: {spirit}")

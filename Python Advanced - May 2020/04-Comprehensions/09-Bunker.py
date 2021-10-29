bunker = {category: {} for category in input().split(', ')}
n = int(input())

for _ in range(n):
    args = input().split(' - ')
    category = args[0]
    item = args[1]
    quantity_quality = args[2].split(';')
    quantity = int(quantity_quality[0].split(':')[1])
    quality = int(quantity_quality[1].split(':')[1])

    bunker[category][item] = quantity, quality

quantities_sum = sum([sum([x[0] for x in list(bunker[category].values())]) for category in bunker])
average_quality = sum([sum([x[1] for x in list(bunker[category].values())]) for category in bunker]) / len(bunker)

print(f'Count of items: {quantities_sum}')
print(f'Average quality: {average_quality:.2f}')
[print(f'{category} -> {", ".join(bunker[category].keys())}') for category in bunker]







heroes = {name: {} for name in input().split(', ')}

args = input().split('-')

while args[0] != 'End':

    name = args[0]
    item = args[1]
    value = int(args[2])

    if item not in heroes[name]:
        heroes[name][item] = value

    args = input().split('-')

[print(f"{name} -> Items: {len(heroes[name])}, Cost: {sum(heroes[name].values())}") for name in heroes]


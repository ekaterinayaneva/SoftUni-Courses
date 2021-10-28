treasure_chest = input().split('|')

command = input().split(' ')
while command[0] != 'Yohoho!':

    if command[0] == 'Loot':
    #    print(command[0])
        for item in command [1::]:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)

    elif command[0] == 'Drop':
        index = int(command[1])
        if 0 <= index < len(treasure_chest):
            treasure_chest.append(treasure_chest.pop(index))

    else:#command[0] == 'Steal':
        stolen_count = int(command[1])
        stolen_items = []

        if stolen_count <= len(treasure_chest):
            stolen_items = treasure_chest[-stolen_count::]
            for i in range(stolen_count):
                treasure_chest.pop()
        else:
            stolen_items = treasure_chest.copy()
            treasure_chest.clear()
        print(', '.join(stolen_items))

    command = input().split()

if treasure_chest:
    average_sum = 0
    for item in treasure_chest:
        average_sum += len(item)
    print(f"Average treasure gain: {average_sum / len(treasure_chest):.2f} pirate credits.")
else:
    print(f"Failed treasure hunt.")

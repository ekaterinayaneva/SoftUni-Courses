inventory = input().split(', ')

args = input().split(' - ')

while args[0] != 'Craft!':

    command = args[0]

    if command == 'Collect':
        item = args[1]
        if item not in inventory:
            inventory.append(item)

    elif command == 'Drop':
        item = args[1]
        if item in inventory:
            inventory.remove(item)

    elif command == 'Combine Items':
        old_new_item = args[1].split(':')
        old_item = old_new_item[0]
        new_item = old_new_item[1]

        if old_item in inventory:
            index = inventory.index(old_item)
            inventory.insert(index + 1, new_item)

    elif command == 'Renew':
        item = args[1]
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)


    args = input().split(' - ')


print(', '.join(inventory))



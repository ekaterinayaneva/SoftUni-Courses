args = input().split('->')

diary = {}

while args[0] != 'END':
    command = args[0]

    if command == 'Add':
        store = args[1]
        items = args[2].split(",")

        if store not in diary:
            diary[store] = []
        for item in items:
            diary[store].append(item)
         #  print(diary)

    elif command == 'Remove':
        store = args[1]
        if store in diary:
            del diary[store]

    args = input().split('->')

diary = dict(sorted(diary.items(), key= lambda v: (-len(v[1]), -len(v[1]))))

print(f'Stores list:')
for store, items in diary.items():
    print(f'{store}')
    for item in items:
        print(f'<<{item}>>')


args = input().split('->')

records = {}

while args[0] != 'END':
    command = args[0]

    if command == 'Add':
        road = args[1]
        racer = args[2]

        if road not in records:
            records[road] = []
        records[road].append(racer)

    elif command == 'Move':
        current_road = args[1]
        racer = args[2]
        next_road = args[3]

        if racer in records[current_road]:
            records[current_road].remove(racer)
            records[next_road].append(racer)

    elif command == 'Close':
        road = args[1]

        del records[road]

    args = input().split('->')

print(f'Practice sessions:')

for road, racers in sorted(records.items(), key=lambda r: (-len(r[1]), r[0])):
    print(f'{road}')
    for racer in racers:
        print(f'++{racer}')


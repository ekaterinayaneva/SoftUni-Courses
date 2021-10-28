targets = list(map(int, input().split()))

args = input().split()

while args[0] != 'End':
    command = args[0]

    if command == 'Shoot':
        index = int(args[1])
        power = int(args[2])

        if index in range(len(targets)):
            targets[index] -= power
            if targets[index] <= 0:
                del targets[index]

    elif command == 'Add':
        index = int(args[1])
        value = int(args[2])

        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print(f"Invalid placement!")

    elif command == 'Strike':
        index = int(args[1])
        radius = int(args[2])

        if index in range(len(targets)) and index + radius in range(len(targets)) and index - radius in range(len(targets)):
            targets = targets[:index-radius:] + targets[index+radius+1::]
        else:
            print(f"Strike missed!" )

    args = input().split()

result = str('|'.join(map(str, targets)))
print(result)

def targets(field):
    targets = 0

    for row in range(len(field)):
        for col in range(len(field)):
            if field[row][col] == 't':
                targets += 1

    return targets


n = int(input())

field = []
plane = []
killed_targets = 0

directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}

for row in range(n):
    line = input().split()
    for col in range(n):
        if line[col] == 'p':
            plane = [row, col]

    field.append(line)


m = int(input())

for _ in range(m):
    line = input().split()

    command = line[0]
    direction = line[1]
    step = int(line[2])

    direction = directions[direction]

    if command == 'move':
        new_position = [plane[0] + (direction[0] * step), plane[1] + (direction[1] * step)]

        if 0 <= new_position[0] < len(field) and 0 <= new_position[1] < len(field):

            if field[new_position[0]][new_position[1]] == '.':
                field[plane[0]][plane[1]] = '.'
                plane = new_position
                field[plane[0]][plane[1]] = 'p'

    elif command == 'shoot':
        target_position = [plane[0] + (direction[0] * step), plane[1] + (direction[1] * step)]

        if 0 <= target_position[0] < len(field) and 0 <= target_position[1] < len(field):

            if field[target_position[0]][target_position[1]] == 't':
                killed_targets += 1

            field[target_position[0]][target_position[1]] = 'x'

            if not targets(field):
                break


targets = targets(field)

if targets:
    print(f'Mission failed! {targets} targets left.')
else:
    print(f'Mission accomplished! All {killed_targets} targets destroyed.')

[print(" ".join(row)) for row in field]

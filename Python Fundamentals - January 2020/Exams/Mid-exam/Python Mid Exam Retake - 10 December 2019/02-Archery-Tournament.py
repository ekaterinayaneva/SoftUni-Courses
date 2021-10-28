targets = list(map(int, input().split("|")))

command = input()
points = 0

while command != 'Game over':
    command_list = command.split('@')

    if command_list[0] == 'Shoot Left':
        index_start = int(command_list[1])
        step = int(command_list[2])

        if 0 <= index_start < len(targets):
            index_shoot = index_start - step
            if index_shoot < 0:
                index_shoot = len(targets) + index_shoot

                while index_shoot < 0:
                    index_shoot = len(targets) + index_shoot

            if targets[index_shoot] >= 5:
                targets[index_shoot] -= 5
                points += 5

            elif 0 <= targets[index_shoot] < 5:
                points += targets[index_shoot]
                targets[index_shoot] = 0

    elif command_list[0] == 'Shoot Right':
        index_start = int(command_list[1])
        step = int(command_list[2])

        if 0 <= index_start < len(targets):
            index_shoot = index_start + step
            if index_shoot > len(targets) - 1:
                index_shoot -= len(targets)

                while index_shoot > len(targets) - 1:
                    index_shoot -= len(targets)

            if targets[index_shoot] >= 5:
                targets[index_shoot] -= 5
                points += 5

            elif 0 <= targets[index_shoot] < 5:
                points += targets[index_shoot]
                targets[index_shoot] = 0

    elif command_list[0] == 'Reverse':
        targets = list(targets[::-1])
    command = input()

targets_to_print = ''
for i in range(len(targets)):
    if i == len(targets) - 1:
        targets_to_print += str(targets[i])
    else:
        targets_to_print += str(targets[i]) + ' - '
print(targets_to_print)
print(f'Iskren finished the archery tournament with {points} points!')

initial_string = [x for x in input()]

n = int(input())

field = []
player = []
directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}


for row in range(n):
    line = [x for x in input()]
    for col in range(n):
        if line[col] == 'P':
            player = [row, col]

    field.append(line)


m = int(input())

for _ in range(m):
    line = input()

    direction = directions[line]
    new_position = [player[0] + direction[0], player[1] + direction[1]]
   # print(new_position)

    if 0 <= new_position[0] < len(field) and 0 <= new_position[1] and len(field):

        if field[new_position[0]][new_position[1]] != '-':
            letter = field[new_position[0]][new_position[1]]
            initial_string.append(letter)

        field[player[0]][player[1]] = '-'
        player = new_position
        field[new_position[0]][new_position[1]] = 'P'

    else:
        if initial_string:
            initial_string.pop()

print(''.join(initial_string))
[print("".join(row)) for row in field]


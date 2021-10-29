def drop_presents(new_pos, matrix, presents):
    row = new_pos[0]
    col = new_pos[1]
    dropped_presents = 0

    if matrix[row][col-1] in 'XV' and presents:
        dropped_presents += 1
        matrix[row][col-1] = '-'
        presents -= 1

    if matrix[row][col+1] in 'XV' and presents:
        dropped_presents += 1
        matrix[row][col + 1] = '-'
        presents -= 1

    if matrix[row-1][col] in 'XV' and presents:
        dropped_presents += 1
        matrix[row - 1][col] = '-'
        presents -= 1

    if matrix[row+1][col] in 'XV' and presents:
        dropped_presents += 1
        matrix[row + 1][col] = '-'
        presents -= 1

    return dropped_presents


def nice_kids(matrix):
    nice_kid = 0

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == 'V':
                nice_kid += 1

    return nice_kid


presents = int(input())
n = int(input())

matrix = []
total_nice_kids = 0

directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}

for row in range(n):
    line = input().split()
    for col in range(n):
        if line[col] == 'S':
            santa_position = [row, col]
        if line[col] == 'V':
            total_nice_kids += 1

    matrix.append(line)

while True:
    line = input()

    if line == 'Christmas morning':
        break

    direction = directions[line]

    new_position = [santa_position[0] + direction[0], santa_position[1] + direction[1]]

    if matrix[new_position[0]][new_position[1]] == 'V':
        presents -= 1
    elif matrix[new_position[0]][new_position[1]] == 'C':
        dropped_presents = drop_presents(new_position, matrix, presents)
        presents -= dropped_presents


    matrix[santa_position[0]][santa_position[1]] = '-'
    santa_position = new_position
    matrix[santa_position[0]][santa_position[1]] = 'S'


    if presents <= 0 and nice_kids(matrix):
        print(f"Santa ran out of presents!")
        break

    if not nice_kids(matrix):       ### mnogo vajno, inache ne vzimame max tochki
        break

nice_kids = nice_kids(matrix)

for row in matrix:
    print(' '.join(row))

if nice_kids:
    print(f"No presents for {nice_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")



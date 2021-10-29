def is_valid(el, rows, cols):
    return 0 <= el[0] < rows and 0 <= el[1] < cols


rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

command = input().split()

while command[0] != 'END':

    if command[0] == 'swap' and len(command) == 5:
        first_el = [int(command[1]), int(command[2])]
        second_el = [int(command[3]), int(command[4])]

        if is_valid(first_el, rows, cols) and is_valid(second_el, rows, cols):
            matrix[first_el[0]][first_el[1]], matrix[second_el[0]][second_el[1]] = \
                matrix[second_el[0]][second_el[1]], matrix[first_el[0]][first_el[1]]
            for row in matrix:
                print(' '.join(str(x) for x in row))
        else:
            print(f'Invalid input!')
    else:
        print(f'Invalid input!')

    command = input().split()



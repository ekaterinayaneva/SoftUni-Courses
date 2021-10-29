n = int(input())

matrix = [[int(x) for x in input().split()] for row in range(n)]

args = input().split()

while args[0] != 'END':
    row = int(args[1])
    col = int(args[2])
    value = int(args[3])

    if 0 <= row < n and 0 <= col < n:

        if args[0] == 'Add':
            matrix[row][col] += value
        elif args[0] == 'Subtract':
            matrix[row][col] -= value

    else:
        print(f"Invalid coordinates")

    args = input().split()

[print(' '.join(str(x) for x in row)) for row in matrix]



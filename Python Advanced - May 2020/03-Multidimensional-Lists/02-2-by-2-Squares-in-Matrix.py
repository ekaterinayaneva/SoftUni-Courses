rows, cols = [int(x) for x in input().split()]

matrix = []
matches = 0

for _ in range(rows):
    line = [x for x in input().split()]
    matrix.append(line)


for row in range(rows - 1):
    for col in range(cols - 1):
        current = matrix[row][col]
        current_right = matrix[row][col+1]
        bottom = matrix[row+1][col]
        bottom_right = matrix[row+1][col+1]

        if current ==  current_right == bottom == bottom_right:
            matches += 1

print(matches)


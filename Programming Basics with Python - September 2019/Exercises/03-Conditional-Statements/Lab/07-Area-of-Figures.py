import math

figure_type = input()
figure_dimension = float(input())


if figure_type == 'square':
    area = figure_dimension * figure_dimension
elif figure_type == 'rectangle':
    b = float(input())
    area = figure_dimension * b
elif figure_type == 'circle':
    area = math.pi * figure_dimension * figure_dimension
elif figure_type == 'triangle':
    b = float(input())
    area = figure_dimension * b / 2

print(f'{area:.3f}')


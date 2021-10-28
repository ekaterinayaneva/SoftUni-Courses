import math
height = int(input())
width = int(input())
percent_not_painting = int(input())

walls_for_painting = (height * width * 4) * ((100 - percent_not_painting) / 100)
walls_for_painting = math.ceil(walls_for_painting)

command = input()
while command != 'Tired!':
    liters_paint = int(command)
    walls_for_painting -= liters_paint

    if walls_for_painting <= 0:
        break

    command = input()

if walls_for_painting > 0:
    print(f"{walls_for_painting} quadratic m left.")
elif walls_for_painting == 0:
    print(f"All walls are painted! Great job, Pesho!")
else:
    print(f"All walls are painted and you have {abs(walls_for_painting)} l paint left!")





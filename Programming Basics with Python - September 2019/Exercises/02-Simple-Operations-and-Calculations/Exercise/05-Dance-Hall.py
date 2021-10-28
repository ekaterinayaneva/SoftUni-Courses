length = float(input())
width = float(input())
wardrobe_side = float(input())

hall_area = (length * 100) * (width * 100)
wardrobe_area = (wardrobe_side * 100) * 2
bench_area = hall_area / 10

free_space = hall_area - wardrobe_area - bench_area

dancers = free_space / (40 + 7000)

import math

print(math.floor(dancers))



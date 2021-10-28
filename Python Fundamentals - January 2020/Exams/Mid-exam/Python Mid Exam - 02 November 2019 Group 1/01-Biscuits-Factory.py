import math

amount_bis_per_worker = int(input())
workers = int(input())
competing_factory = int(input())

sum_of_biscuits = 0

for day in range(30):
    bis_per_day = workers * amount_bis_per_worker

    if day % 3 == 0:
        bis_per_day *= 0.75

    sum_of_biscuits += bis_per_day

print(f"You have produced {math.floor(sum_of_biscuits)} biscuits for the past month.")

percentage = abs(sum_of_biscuits - competing_factory) / competing_factory * 100

if sum_of_biscuits > competing_factory:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")


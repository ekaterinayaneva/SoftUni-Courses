n = int(input())

capacity = 255
liters_in_the_tank = 0

for num in range(n):
    liters_of_water = int(input())

    if capacity >= liters_of_water:
        capacity -= liters_of_water
        liters_in_the_tank += liters_of_water

    elif liters_of_water > capacity:
        print(f'Insufficient capacity!')

print(liters_in_the_tank)



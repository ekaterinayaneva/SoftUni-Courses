number_of_cars = int(input())

cars = {}

for num in range(number_of_cars):
    car_input = input().split('|')
    car = car_input[0]
    mileage = int(car_input[1])
    fuel = int(car_input[2])

    cars[car] = []
    cars[car].append(mileage)
    cars[car].append(fuel)


args = input()

while args != 'Stop':
    args = args.split(' : ')
    command = args[0]

    if command == 'Drive':
 #       print(command)
        car = args[1]
        distance = int(args[2])
        fuel = int(args[3])

        if cars[car][1] < fuel:
            print(f"Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car][0] >= 100000:
                del cars[car]
                print(f"Time to sell the {car}!")

    elif command == 'Refuel':
        car = args[1]
        fuel = int(args[2])

        if cars[car][1] + fuel > 75:
            print(f"{car} refueled with {75 - cars[car][1]} liters")
            cars[car][1] = 75
            args = input()
            continue

        cars[car][1] += fuel
        print(f"{car} refueled with {fuel} liters")

    elif command == 'Revert':
        car = args[1]
        kilometers = int(args[2])

        cars[car][0] -= kilometers
        if cars[car][0] < 10000:
            cars[car][0] = 10000
            args = input()
            continue
        print(f"{car} mileage decreased by {kilometers} kilometers")


    args = input()

for car, value in sorted(cars.items(), key=lambda v: (-v[1][0], v[0])):
    print(f"{car} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")



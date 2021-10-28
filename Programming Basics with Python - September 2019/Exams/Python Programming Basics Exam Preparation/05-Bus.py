first_passengers = int(input())
bus_stops = int(input())

controllers = 0
passengers = 0

for stops in range(bus_stops):
    passengers_out = int(input())
    passengers_in = int(input())
    if stops % 2 == 1:
        controllers = -2
    elif stops % 2 == 0:
        controllers = 2

    on_off = passengers_in - passengers_out + controllers
    passengers += on_off

total_passengers = first_passengers + passengers
print(f'The final number of passengers is : {total_passengers}')



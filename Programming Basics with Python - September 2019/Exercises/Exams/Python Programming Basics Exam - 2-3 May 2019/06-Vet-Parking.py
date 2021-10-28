days = int(input())
hours = int(input())

total = 0

for day in range(1, days + 1):
    is_day_even = False
    is_hour_even = False
    parking_price = 0

    if day % 2 == 0:
        is_day_even = True

    if hours % 2 == 0:
        is_hour_even = True

    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            parking_price += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            parking_price += 1.25
        else:
            parking_price += 1

    total += parking_price
    print(f'Day: {day} - {parking_price:.2f} leva')

print(f'Total: {total:.2f} leva')

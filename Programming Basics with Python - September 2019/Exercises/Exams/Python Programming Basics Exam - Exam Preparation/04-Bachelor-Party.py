singer_price = int(input())

guest_counter = 0
reservations = 0
couvert_price = 0

command = input()
while command != 'The restaurant is full':
    guests = int(command)
    guest_counter += guests
    couvert_price = 100
    if guests >= 5:
        couvert_price = 70

    current_sum = guests * couvert_price
    reservations += current_sum

    command = (input())

if reservations >= singer_price:
    leva_left = reservations - singer_price
    print(f"You have {guest_counter} guests and {leva_left} leva left.")
else:
    print(f"You have {guest_counter} guests and {reservations} leva income, but no singer.")



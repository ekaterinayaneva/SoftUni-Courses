width = int(input())
length = int(input())
height = int(input())
boxes = input()

apartment_volume = width * length * height

boxes_volume = 0
is_free = True



while not boxes == 'Done':
    boxes = int(boxes)
    boxes_volume += boxes

    if boxes_volume > apartment_volume:
        is_free = False
        break

    boxes = (input())

difference = abs(apartment_volume - boxes_volume)
if is_free:
    print(f"{difference} Cubic meters left.")
else:
    print(f"No more free space! You need {difference} Cubic meters more.")

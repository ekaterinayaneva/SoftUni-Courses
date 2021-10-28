import math

width = float(input())
length = float(input())
height = float(input())
astronauts_height = float(input())

racket_volume = width * length * height
room_volume = (astronauts_height + 0.4) * 2 * 2
free_space = racket_volume / room_volume

free_space = math.floor(free_space)

if 3 < free_space < 10:
    print(f"The spacecraft holds {free_space} astronauts.")
elif free_space < 3:
    print(f"The spacecraft is too small.")
elif free_space > 10:
    print(f"The spacecraft is too big.")




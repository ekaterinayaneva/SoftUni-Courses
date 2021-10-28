length = int(input())
width = int(input())
height = int(input())
percent_occupied_volume = float(input())

akquarium_volume = length * width * height

litters = akquarium_volume * 0.001

percent = percent_occupied_volume * 0.01

needed_liters = litters - litters * percent

print(f'{needed_liters:.3f}')







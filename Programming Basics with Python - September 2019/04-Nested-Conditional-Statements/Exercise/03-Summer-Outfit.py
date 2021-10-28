degrees = int(input())
day_time = input()

shoes = str
outfit = str
if day_time == 'Morning':
    if 10 <= degrees <= 18:
        shoes = 'Sneakers'
        outfit = 'Sweatshirt'
    elif 18 < degrees <= 24:
        shoes = 'Moccasins'
        outfit = 'Shirt'
    elif degrees >= 25:
        shoes = 'Sandals'
        outfit = 'T-Shirt'
elif day_time == 'Afternoon':
    if 10 <= degrees <= 18:
        shoes = 'Moccasins'
        outfit = 'Shirt'
    elif 18 < degrees <= 24:
        shoes = 'Sandals'
        outfit = 'T-Shirt'
    elif degrees >= 25:
        shoes = 'Barefoot'
        outfit = 'Swim Suit'
elif day_time == 'Evening':
    if 10 <= degrees <= 18:
        shoes = 'Moccasins'
        outfit = 'Shirt'
    elif 18 < degrees <= 24:
        shoes = 'Moccasins'
        outfit = 'Shirt'
    elif degrees >= 25:
        shoes = 'Moccasins'
        outfit = 'Shirt'

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")





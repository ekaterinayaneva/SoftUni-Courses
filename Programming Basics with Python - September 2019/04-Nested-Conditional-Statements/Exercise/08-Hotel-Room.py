month = input()
nights = int(input())

studio = 0
apartment = 0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if 7 < nights < 15:
        studio = studio * 0.95
    elif nights > 14:
        studio = studio * 0.7
        apartment = apartment * 0.9
elif month == 'June' or month == 'September':
    studio = 75.2
    apartment = 68.7
    if nights > 14:
        studio = studio * 0.8
        apartment = apartment * 0.9
elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77
    if nights > 14:
        apartment = apartment * 0.9

studio_price = nights * studio
apartment_price = nights * apartment

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')



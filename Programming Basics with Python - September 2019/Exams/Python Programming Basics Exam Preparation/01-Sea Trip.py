day_coats_food = float(input())
day_coasts_souvenirs = float(input())
day_coats_hotel = float(input())

gas = 420 / 100 * 7
gas = gas * 1.85

food_souvenirs = (3 * day_coats_food) + (3 * day_coasts_souvenirs)

first_day_hotel = day_coats_hotel * 0.9
second_day_hotel = day_coats_hotel * 0.85
third_day_hotel = day_coats_hotel * 0.8

total = gas + food_souvenirs + first_day_hotel + second_day_hotel + third_day_hotel

print(f'Money needed: {total:.2f}')






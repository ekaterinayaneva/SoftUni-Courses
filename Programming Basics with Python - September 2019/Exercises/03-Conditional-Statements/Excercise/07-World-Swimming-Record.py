import math

record = float(input())
distance = float(input())
time = float(input())

seconds = distance * time

seconds_plus = math.floor(distance / 15) * 12.5

counting_time = seconds + seconds_plus

if counting_time >= record:
    left_time = counting_time - record
    print(f'No, he failed! He was {left_time:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {counting_time:.2f} seconds.')


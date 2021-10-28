import sys
n = int(input())

highest_rating = -sys.maxsize
lowest_rating = sys.maxsize
name_highest = ''
name_lowest = ''
rating_sum = 0

for x in range(n):
    movie = input()
    rating = float(input())
    rating_sum += rating

    if rating > highest_rating:
        highest_rating = rating
        name_highest = movie

    elif rating < lowest_rating:
        lowest_rating = rating
        name_lowest = movie

average_rating = rating_sum / n

print(f"{name_highest} is with highest rating: {highest_rating:.1f}")
print(f"{name_lowest} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")




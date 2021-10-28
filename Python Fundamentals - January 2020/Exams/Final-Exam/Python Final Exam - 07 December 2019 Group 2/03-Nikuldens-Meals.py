text_input = input().split('-')

liked_meals = {}
unliked_meals = 0

while text_input[0] != 'Stop':
    command = text_input[0]
    guest = text_input[1]
    meal = text_input[2]


    if command == 'Like':
        if guest not in liked_meals:
            liked_meals[guest] = []
        if meal not in liked_meals[guest]:
            liked_meals[guest].append(meal)
    elif command == 'Unlike':
        if guest not in liked_meals:
            print(f"{guest} is not at the party.")
        elif meal not in liked_meals[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            liked_meals[guest].remove(meal)
            print(f"{guest} doesn't like the {meal}.")
            unliked_meals += 1

    text_input = input().split('-')

liked_meals = dict(sorted(liked_meals.items(), key=lambda v: (-len(v[1]), v[0])))

for guest, meals in liked_meals.items():
    print(f'{guest}: {", ".join(meals)}')

print(f'Unliked meals: {unliked_meals}')




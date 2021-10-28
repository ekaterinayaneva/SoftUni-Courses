rooms = int(input())

free_chairs = 0
needed_chairs = 0

for room in range(1, rooms + 1):
    condition = input().split()

    chairs = len(condition[0])
    list_people = (int(condition[1]))

    if chairs < list_people:
        needed_chairs = list_people - chairs
        print(f"{needed_chairs} more chairs needed in room {room}")

    elif chairs >= list_people:
        free_chr = chairs - list_people
        free_chairs += free_chr

if needed_chairs == 0:
    print(f"Game On, {free_chairs} free chairs left")


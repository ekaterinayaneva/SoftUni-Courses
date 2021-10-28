actor_name = input()
academy_points = float(input())
appraisers_number = int(input())

points = 0
total_points = 0

for x in range(appraisers_number):
    appraisers_name = input()
    appraisers_points = float(input())

    points = len(appraisers_name) * appraisers_points / 2

    total_points += points

    if total_points + academy_points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points + academy_points:.1f}!")
        break

if total_points + academy_points < 1250.5:
    print(f"Sorry, {actor_name} you need {1250.5-(total_points + academy_points):.1f} more!")


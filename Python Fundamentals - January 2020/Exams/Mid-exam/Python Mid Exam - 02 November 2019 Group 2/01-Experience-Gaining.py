needed_experience = float(input())
battles = int(input())

battle_counter = 0
collected_experience = 0

for battle in range(1, battles + 1):
    battle_counter += 1
    experience_per_battle = float(input())

    if battle % 3 == 0:
        experience_per_battle *= 1.15

    if battle % 5 == 0:
        experience_per_battle *= 0.9

    collected_experience += experience_per_battle
    if collected_experience >= needed_experience:
        print(f"Player successfully collected his needed experience for {battle_counter} battles.")
        break

else:
    print(f"Player was not able to collect the needed experience, {needed_experience - collected_experience:.2f} more needed.")

    
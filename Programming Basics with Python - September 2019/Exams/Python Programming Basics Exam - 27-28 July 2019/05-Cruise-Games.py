import math
player_name = input()
played_games = int(input())

counter_v = 0
counter_t = 0
counter_b = 0
volleyball_points = 0
tennis_points = 0
badminton_points = 0
for x in range(played_games):
    game_name = input()
    points = int(input())

    if game_name == "volleyball":
        volleyball_points += points * 1.07
        counter_v += 1
       # volleyball_points = volleyball_points * 1.07    dava otklonenie v rezultata

    elif game_name == "tennis":
        tennis_points += points * 1.05
        counter_t += 1

    elif game_name == "badminton":
        badminton_points += points * 1.02
        counter_b += 1

end_points_volleyball = math.floor(volleyball_points / counter_v)
end_points_tennis = math.floor(tennis_points / counter_t)
end_points_badminton = math.floor(badminton_points / counter_b)
total_points = math.floor(volleyball_points + tennis_points + badminton_points)

if end_points_volleyball >= 75 and end_points_tennis >= 75 and end_points_badminton >= 75:
    print(f"Congratulations, {player_name}! You won the cruise games with {total_points} points.")
else:
    print(f"Sorry, {player_name}, you lost. Your points are only {total_points}.")



football_team = input()
played_games = int(input())

counter_W = 0
counter_D = 0
counter_L = 0
points_W = 0
points_D = 0

total_points = 0

for game in range(played_games):
    result = input()

    if result == 'W':
        counter_W += 1
    elif result == 'D':
        counter_D += 1
    elif result == 'L':
        counter_L += 1

points_W = counter_W * 3
points_D = counter_D * 1

total_points = points_W + points_D

if played_games > 0:
    print(f"{football_team} has won {total_points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {counter_W}")
    print(f"## D: {counter_D}")
    print(f"## L: {counter_L}")
    percent_win_games = (100 / played_games * counter_W)
    print(f"Win rate: {percent_win_games:.2f}%")
else:
    print(f"{football_team} hasn't played any games during this season.")



cards = input().split(' ')

team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_a_count = 11
team_b_count = 11

for card in cards:
    card = card.split('-')
    team = card[0]
    player = int(card[1])

    if team == 'A':
        if player in team_a:
            team_a.remove(player)
            team_a_count -= 1
    else:
        if player in team_b:
            team_b.remove(player)
            team_b_count -= 1


print(f"Team A - {team_a_count}; Team B - {team_b_count}")

if team_a_count < 7 or team_b_count < 7:
    print(f"Game was terminated")



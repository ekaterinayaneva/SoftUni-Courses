sold_games = int(input())

counter_Hearthstone = 0
counter_Fornite = 0
counter_Overwatch = 0
counter_Others = 0

for n in range(sold_games):
    game_name = input()

    if game_name == 'Hearthstone':
        counter_Hearthstone += 1
    elif game_name == 'Fornite':
        counter_Fornite += 1
    elif game_name == 'Overwatch':
        counter_Overwatch += 1
    elif game_name != 'Hearthstone' and game_name != 'Fornite' and game_name != 'Overwatch':
        counter_Others += 1

counter_Hearthstone = (100 / sold_games * counter_Hearthstone)
counter_Fornite = (100 / sold_games * counter_Fornite)
counter_Overwatch = (100 / sold_games * counter_Overwatch)
counter_Others = (100 / sold_games * counter_Others)

print(f'Hearthstone - {counter_Hearthstone:.2f}%')
print(f'Fornite - {counter_Fornite:.2f}%')
print(f'Overwatch - {counter_Overwatch:.2f}%')
print(f'Others - {counter_Others:.2f}%')





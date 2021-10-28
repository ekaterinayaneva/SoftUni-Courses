points = int(input())

moves = 0
has_win = False
target_sector = input()
while True:

    moves += 1

    if target_sector == "bullseye":
        has_win = True
        print(f"Congratulations! You won the game with a bullseye in {moves} moves!")
        break

    if points < 0:
        print(f"Sorry, you lost. Score difference: {abs(points)}.")
        break

    target_points = int(input())

    if target_sector == "number section":
        target_points = target_points
    elif target_sector == "double ring":
        target_points = target_points * 2
    elif target_sector == "triple ring":
        target_points = target_points * 3

    points -= target_points

    if points == 0:
        print(f"Congratulations! You won the game in {moves} moves!")
        break

    target_sector = input()


neighborhood = list(map(int, input().split('@')))

command = input().split()

cupid_position = 0
valentines_houses = 0

while command[0] != 'Love!':

    jump_length = int(command[1])

    if cupid_position + jump_length >= len(neighborhood):
        cupid_position = 0

    else:
        cupid_position += jump_length

    if neighborhood[cupid_position] != 0:
        neighborhood[cupid_position] -= 2
        if neighborhood[cupid_position] == 0:
            print(f"Place {cupid_position} has Valentine's day.")
            valentines_houses += 1

    else: #string_input[cupid_position] < 0:
        print(f"Place {neighborhood[cupid_position]} already had Valentine's day.")

    command = input().split()

print(f"Cupid's last position was {cupid_position}.")

if valentines_houses == len(neighborhood):
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {len(neighborhood) - valentines_houses} places.")


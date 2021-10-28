name = input()


winner_value = 0
winner_name = str

while name != 'STOP':
    sum = 0
    for letter in name:
        ascii_value = ord(letter)
        sum += ascii_value


    if sum > winner_value:
        winner_value = sum
        winner_name = name
    name = input()

print(f'Winner is {winner_name} - {winner_value}! ')






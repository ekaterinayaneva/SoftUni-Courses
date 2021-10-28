points = 0
sum = 0
winner_sum = 0
winner_name = ''

while True:
    name = input()

    if name == 'Stop':
        print(f"The winner is {winner_name} with {winner_sum} points!")
        break

    for letter in name:
        number = int(input())

        ascii_value = ord(letter)

        if ascii_value == number:
            points = 10
        else:
            points = 2

        sum += points

    if sum >= winner_sum:
        winner_sum = sum
        winner_name = name
        sum = 0


cards = input().split(':')
deck = []
instructions = input().split(' ')

while instructions[0] != 'Ready':
    command = instructions[0]
    #card_name = instructions[1]
   # card_name_2 = instructions[2]
    #index = int(instructions[2])

    if command == 'Add':
        card_name = instructions[1]
        if card_name in cards:
            deck.append(card_name)
        else:
            print(f"Card not found.")
    elif command == 'Insert':
        card_name = instructions[1]
        index = int(instructions[2])
        if card_name in cards:
            if 0 <= index < len(deck):
                deck.insert(index, card_name)
            else:print(f'Error!')
        else:
            print(f"Error!")
    elif command == 'Remove':
        card_name = instructions[1]
        if card_name in deck:
            deck.remove(card_name)
        else:
            print(f"Card not found.")
    elif command == 'Swap':
        card_name = instructions[1]
        card_name_2 = instructions[2]
        for i, s in enumerate(deck):
            if card_name in s:
                deck[i] = s.replace(card_name, card_name_2)
            elif card_name_2 in s:
                deck[i] = s.replace(card_name_2, card_name)
       # i = deck.index(card_name)
       # deck[i:i + 2] = deck[i + 1:i - 1:-1]
    elif command == 'Shuffle':
        deck.reverse()

    instructions = input().split(' ')

print(' '.join(deck))

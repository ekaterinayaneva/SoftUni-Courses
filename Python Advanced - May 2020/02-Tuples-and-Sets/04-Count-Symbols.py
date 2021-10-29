text = input()

character_count = {}

for character in text:
    if character not in character_count:
        character_count[character] = 0
    character_count[character] += 1

for key,value in sorted(character_count.items()):
    print(f'{key}: {value} time/s')



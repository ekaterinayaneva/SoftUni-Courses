input_line = input().split()

heroes = {}

while input_line[0] != 'End':
    command = input_line[0]

    if command == 'Enroll':
        hero_name = input_line[1]

        if hero_name not in heroes:
            heroes[hero_name] = []
        else:
            print(f'{hero_name} is already enrolled.')

    elif command == 'Learn':
        hero_name = input_line[1]
        spell_name = input_line[2]

        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell_name in heroes[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            heroes[hero_name].append(spell_name)

    elif command == 'Unlearn':
        hero_name = input_line[1]
        spell_name = input_line[2]

        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in heroes[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            heroes[hero_name].remove(spell_name)


    input_line = input().split()

heroes = dict(sorted(heroes.items(), key=lambda v: (-len(v[1]), v[0])))

print(f'Heroes:')
for hero, value in heroes.items():
    print(f'== {hero}: {", ".join(value)}')




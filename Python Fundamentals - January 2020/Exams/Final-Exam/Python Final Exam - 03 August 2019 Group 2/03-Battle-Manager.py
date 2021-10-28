args = input().split(':')

records = {}

while args[0] != 'Results':
    command = args[0]

    if command == 'Add':
        person = args[1]
        health = int(args[2])
        energy = int(args[3])
        if person not in records:
            records[person] = []
            records[person].append(health)
            records[person].append(energy)
        else:
            records[person][0] += health

    elif command == 'Attack':
        attacker = args[1]
        defender = args[2]
        damage = int(args[3])
        if attacker in records and defender in records:

            records[defender][0] -= damage
            if records[defender][0] <= 0:
                del records[defender]
                print(f"{defender} was disqualified!")

            records[attacker][1] -= 1
            if records[attacker][1] == 0:
                del records[attacker]
                print(f"{attacker} was disqualified!")
    elif command == 'Delete':
        username = args[1]

        if username == 'All':
            records = {}
        else:
            del records[username]



    args = input().split(':')

print(f'People count: {len(records)}')

for person, value in sorted(records.items(), key=lambda v: (-v[1][0], v[0])):
    print(f'{person} - {value[0]} - {value[1]}')

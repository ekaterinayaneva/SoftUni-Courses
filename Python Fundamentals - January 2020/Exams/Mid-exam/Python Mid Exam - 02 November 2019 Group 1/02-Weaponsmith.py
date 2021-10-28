weapon = input().split('|')

instructions = input().split(' ')
even = []
odd = []
name = []
while instructions[0] != 'Done':
    command = instructions[1]

    if command == 'Left':
        index = int(instructions[2])
        index_1 = index - 1
        if 1 <= index < len(weapon):
            weapon[index], weapon[index_1] = weapon[index_1], weapon[index]
    elif command == 'Right':
        index = int(instructions[2])
        index_1 = index + 1
        if 0 <= index < len(weapon) -1:
            weapon[index], weapon[index_1] = weapon[index_1], weapon[index]
    elif command == 'Even':
        even = weapon[0::2]
        print(' '.join(even))
    elif command == 'Odd':
        odd = weapon[1::2]
        print(' '.join(odd))

    instructions = input().split()

name = (''.join(weapon))
print(f"You crafted {name}!")

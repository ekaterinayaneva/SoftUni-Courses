initial_list = input().split('!')

instructions = input().split(' ')

while instructions[0] != "Go Shopping!":
    command = instructions[0]

    if command == 'Urgent':
        item = instructions[1]
        if item in initial_list:
            continue
        else:
            initial_list.insert(0, item)
    elif command == 'Unnecessary':
        item = instructions[1]
        if item in initial_list:
            initial_list.remove(item)
        else:
            continue
    elif command == 'Correct':
        old_item = instructions[1]
        new_item = instructions[2]
        if old_item in initial_list:
            for i in range(len(initial_list)):
                if old_item == initial_list[i]:
                    initial_list[i] = new_item
        else:
            continue
    elif command == 'Rearrange':
        item = instructions[1]
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)

    instructions = input().split(' ')

print(', '.join(initial_list))


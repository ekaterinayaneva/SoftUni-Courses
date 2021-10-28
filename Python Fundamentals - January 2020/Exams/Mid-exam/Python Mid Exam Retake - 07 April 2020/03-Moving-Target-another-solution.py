targets = list(map(int, input().split()))

index = input()
needed_value = 0
shot_targets = 0

while index != 'End':
    index = int(index)

    if index in range(len(targets)):
        shot_targets += 1
        needed_value = targets[index]
        targets[index] = -1

        for i in targets:
            if i > needed_value:
                reduces_index = targets.index(i)
                targets[reduces_index] -= needed_value

            elif 0 <= i <= needed_value:
                increased_index = targets.index(i)
                targets[increased_index] += needed_value


    index = input()

result = str(' '.join(map(str, targets)))

print(f"Shot targets: {shot_targets} -> {result}")




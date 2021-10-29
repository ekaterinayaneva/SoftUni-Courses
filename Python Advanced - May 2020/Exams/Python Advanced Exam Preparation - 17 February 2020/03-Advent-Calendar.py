def fix_calendar(numbers):
    for num in range(len(numbers)):
        for next_num in range(len((numbers))):

            if numbers[num] < numbers[next_num]:
                numbers[num], numbers[next_num] = numbers[next_num], numbers[num]

    return numbers



numbers = [3, 2, 1, 20, 15, 6, 3]
fixed = fix_calendar(numbers)
print(fixed)


n = int(input())

longest_intersection = set()

for _ in range(n):
    line = input().split('-')
    range_one = line[0].split(',')
    range_two = line[1].split(',')

    start_range_one = int(range_one[0])
    end_range_one = int(range_one[1])

    start_range_two = int(range_two[0])
    end_range_two = int(range_two[1])

    set_one = set([x for x in range(start_range_one, end_range_one + 1)])
    set_two = set([x for x in range(start_range_two, end_range_two + 1)])

    intersection = set_one & set_two

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

converted_intersection = [str(x) for x in longest_intersection]
print(f"Longest intersection is [{', '.join(converted_intersection)}] with length {len(longest_intersection)}")

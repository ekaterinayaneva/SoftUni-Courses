n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n+1):
    name = input()

    sum_of_name = sum([ord(x) for x in name]) // i

    if sum_of_name % 2 == 0:
        even_set.add(sum_of_name)
    else:
        odd_set.add(sum_of_name)

sum_of_even = sum(even_set)
sum_of_odd = sum(odd_set)

if sum_of_even == sum_of_odd:
    union_values = even_set | odd_set
    print(', '.join([str(x) for x in union_values]))
elif sum_of_odd > sum_of_even:
    different_values = odd_set.difference(even_set)
    print(', '.join([str(x) for x in different_values]))
else:
    symmetric_different_values = even_set.symmetric_difference(odd_set)
    print(', '.join([str(x) for x in symmetric_different_values]))




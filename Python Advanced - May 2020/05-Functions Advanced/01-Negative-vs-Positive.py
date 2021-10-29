numbers = list(map(int, input().split()))

negative = sum(filter(lambda x: x < 0, numbers))
positive = sum(filter(lambda x: x > 0, numbers))

#negative_sum = sum(negative)
#positive_sum = sum(positive)

print(negative)
print(positive)

if abs(negative) > positive:
    print(f'The negatives are stronger than the positives')
else:
    print(f'The positives are stronger than the negatives')



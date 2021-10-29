numbers = input().split('|')

result = [x for x in numbers[::-1] for x in x.split()]

print(' '.join(result))

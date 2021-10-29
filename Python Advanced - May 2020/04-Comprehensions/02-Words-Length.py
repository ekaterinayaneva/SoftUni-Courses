strings = input().split(', ')

result = [f'{x} -> {len(x)}' for x in strings]

print(', '.join(result))


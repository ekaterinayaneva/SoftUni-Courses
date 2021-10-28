import re

n = int(input())

pattern = r"\|([A-Z]{4,})\|:#([A-Za-z]+\s[A-Za-z]+)#"

for num in range(n):
    valid_name = input()

    match = re.match(pattern, valid_name)

    if match is None:
        print(f"Access denied!")
        continue

    print(f"{match[1]}, The {match[2]}")
    print(f'>> Strength: {len(match[1])}')
    print(f'>> Armour: {len(match[2])}')

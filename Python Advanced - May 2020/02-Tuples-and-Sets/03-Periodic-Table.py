n = int(input())

chemical_elements = set()

for _ in range(n):
    elements = input().split()
    for element in elements:
        chemical_elements.add(element)

print('\n'.join(chemical_elements))


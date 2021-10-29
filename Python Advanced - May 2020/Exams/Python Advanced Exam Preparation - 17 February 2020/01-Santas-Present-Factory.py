from collections import deque

materials = [int(x) for x in input().split()]
magics = deque([int(x) for x in input().split()])

presents = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
crafted_present = {'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0}

while magics and materials:
    material = materials[-1]
    magic = magics[0]

    if material == 0:
        materials.pop()
        continue

    if magic == 0:
        magics.popleft()
        continue

    result = material * magic

    if result in presents:
        materials.pop()
        magics.popleft()
        present = presents[result]
        crafted_present[present] += 1

    elif result < 0:
        diff = magic + material
        materials.pop()
        magics.popleft()
        materials.append(diff)

    elif result > 0:
        magics.popleft()
        materials.append(materials.pop() + 15)

if (crafted_present['Doll'] and crafted_present['Wooden train']) or (crafted_present['Teddy bear'] and crafted_present['Bicycle']):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials:
    print(f'Materials left: {", ".join([str(x) for x in reversed(materials)])}')
if magics:
    print(f'Magic left: {", ".join([str(x) for x in magics])}')

for toy, value in sorted(crafted_present.items()):
    if value:
        print(f"{toy}: {value}")






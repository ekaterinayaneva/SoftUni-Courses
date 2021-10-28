import re

pattern = r">>(?P<item>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)!(?P<count>\d+)"

bought_furniture = []
total_sum = 0

while True:
    args = input()

    if args == 'Purchase':
        break

    match = re.finditer(pattern, args)

    for item in match:
        bought_furniture.append(item.group('item'))

        total_sum += float(item.group('price')) * int(item.group('count'))

print(f"Bought furniture:")
for item in bought_furniture:
    print(item)

print(f"Total money spend: {total_sum:.2f}")

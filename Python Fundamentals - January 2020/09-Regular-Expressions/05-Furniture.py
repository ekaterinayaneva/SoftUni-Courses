import re

pattern = r">>([a-z]+)<<([0-9]+[\.0-9]*)!(\d+)"

bought_furniture = []
total_sum = 0

while True:
    args = input()

    if args == 'Purchase':
        break

    match = re.finditer(pattern, args, re.IGNORECASE)

    for item in match:
        bought_furniture.append(item[1])

        total_sum += float(item[2]) * int(item[3])

print(f"Bought furniture:")
for item in bought_furniture:
    print(item)

print(f"Total money spend: {total_sum:.2f}")

import re

n = int(input())
group = ''

pattern_barcode = r"([@])#+([A-Z][A-Za-z0-9]+[A-Z])\1#+"
pattern_numbers = r"\d"

for i in range(n):
    barcodes = input()

    match = re.match(pattern_barcode, barcodes)

    if match is None:
        print(f"Invalid barcode")
        continue

    number_matches = re.findall(pattern_numbers, match[2])
    if not number_matches:
        print(f"Product group: 00")
    else:
        result = (str(''.join(map(str, number_matches))))
        print(f"Product group: {result}")
     #   continue




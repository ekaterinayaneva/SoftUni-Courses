import re

decrypt_geohashcode = []

while True:
    message = input()

    pattern = r"^([#|\$|%|&|\*])([A-Za-z]+)\1=(\d+)!!(.+)"

    match = re.match(pattern, message)


    if match and len(match.group(4)) == int(match.group(3)):

        for ch in match.group(4):
            decrypt_ch = ord(ch) + len(match.group(4))
            decrypt_geohashcode.append(chr(decrypt_ch))

        print(f"Coordinates found! {match[2]} -> {''.join(decrypt_geohashcode)}")
        break

    else:
        print(f"Nothing found!")

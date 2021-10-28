import re

message = input()

mountain_name = []

while message != 'Last note':

    pattern = r"([A-z|!|@|#|$|?]+)=(\d+)<<(.+)"

    match = re.match(pattern, message)

    if match and len(match.group(3)) == int(match.group(2)):

        for ch in match.group(1):
            if ch == '!' or ch == '@' or ch == '#' or ch == '$' or ch == '?':
                continue
            else:
                mountain_name.append(ch)

        print(f"Coordinates found! {''.join(mountain_name)} -> {match[3]}")

    else:
        print("Nothing found!")


    message = input()


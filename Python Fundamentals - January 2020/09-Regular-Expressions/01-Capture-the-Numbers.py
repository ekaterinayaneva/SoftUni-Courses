import re

pattern = r"\d+"

text = input()

while True:

    if not text:
        break

    numbers = re.findall(pattern, text)
    for num in numbers:
        print(num, end=' ')

    text = input()

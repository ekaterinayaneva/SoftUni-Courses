import re

regex = re.compile(r"(::|\*\*)([A-Z][a-z]{2,})\1")

text = input()
cool = 1

for i in text:
    if i.isdigit():
        cool *= int(i)


print(f"Cool threshold: {cool}")
print(f"{len(regex.findall(text))} emojis found in the text. The cool ones are:")


for emo in regex.finditer(text):
    coolness = 0
    for i in emo.group(2):
        coolness += ord(i)
    if coolness > cool:
        print(emo.group(0))


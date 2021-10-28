import re

pattern = r"\b(_)([a-zA-Z0-9]+\b)"

text = input()

variable_names = []

matches = re.findall(pattern, text)
for match in matches:
   # print(match)
    variable_names.append(match[1])

print(','.join(variable_names))


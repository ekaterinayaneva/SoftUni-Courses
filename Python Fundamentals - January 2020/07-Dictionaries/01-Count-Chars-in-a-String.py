def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        my_dict[key] = def_value


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


text = input()

my_dict = {}

for char in text:
    if char == ' ':
        continue

    validate_key_existing(my_dict, char)

    my_dict[char] += 1

print_dict(my_dict, '{} -> {}')


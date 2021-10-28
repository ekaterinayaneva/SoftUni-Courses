def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(v))

company_name = {}

while True:
    instructions = input().split(' -> ')

    if instructions[0] == 'End':
        break

    company = instructions[0]
    employees_id = instructions[1]

    validate_key_existing(company_name, company, [])

    if employees_id not in company_name[company]:
        company_name[company].append(employees_id)


company_name = dict(sorted(company_name.items(), key=lambda x: x[0]))

for k, v in company_name.items():
    print(k)
    for i in v:
        print(f'-- {i}')

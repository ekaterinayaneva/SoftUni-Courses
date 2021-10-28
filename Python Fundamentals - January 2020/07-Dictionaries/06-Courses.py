def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value

courses = {}

instruction = input().split(' : ')

while instruction[0] != 'end':
    course = instruction[0]
    student = instruction[1]

    validate_key_existing(courses, course, [])
    courses[course].append(student)

    instruction = input().split(' : ')

courses = dict(sorted(courses.items(), key=lambda x: (-len(x[1]))))

for k, v in courses.items():
    print(f'{k}: {len(v)}')
    for i in sorted(v):
        print(f'-- {i}')


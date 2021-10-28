def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


n = int(input())

students_result = {}

for i in range(n):
    student = input()
    grade = float(input())

    validate_key_existing(students_result, student, [])
    students_result[student].append(grade)

average_grades = {}

for k, v in students_result.items():
    average_gr = sum(v) / len(v)

    if average_gr < 4.5:
        continue

    average_grades[k] = average_gr

average_grades = dict(sorted(average_grades.items(), key=lambda el: -el[1]))
print_dict(average_grades, '{} -> {:.2f}')



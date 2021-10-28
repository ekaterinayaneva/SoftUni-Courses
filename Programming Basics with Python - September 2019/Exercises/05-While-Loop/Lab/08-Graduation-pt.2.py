name = input()

class_counter = 1
average_score = 0
bad_grade_counter = 0

while class_counter <= 12:

    if bad_grade_counter == 2:
        print(f'{name} has been excluded at {class_counter} grade')
        break

    evaluation = float(input())

    if evaluation < 4:
        bad_grade_counter += 1

    elif evaluation >= 4:
        class_counter +=1
        average_score += evaluation

if bad_grade_counter < 2:
    print(f'{name} graduated. Average grade: {(average_score / 12):.2f}')

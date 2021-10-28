jury = int(input())
presentation = ''
evaluation = 0

while presentation != 'Finish':
    for n in range(jury):
        evaluation = float(input())

    evaluations += evaluation

    student_middle_assessment = evaluation / jury
    print(f'{presentation} - {student_middle_assessment}.')






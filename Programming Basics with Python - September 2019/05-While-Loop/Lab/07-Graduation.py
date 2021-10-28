name = input()

class_counter = 1
average_score = 0

while class_counter <= 12:
    evaluation = float(input())
    if evaluation >= 4:
        class_counter +=1
        average_score += evaluation
    else:
        counter = 0

print(f'{name} graduated. Average grade: {(average_score / 12):.2f}')



max_bad_grades = int(input())

problem_counter = 0
average_score = 0
number_of_problems = 0
has_failed = False
last_problem = str

problem_name = input()

while not problem_name == 'Enough':
    grade = int(input())
    average_score += grade
    number_of_problems += 1
    last_problem = problem_name

    if grade <= 4:
        problem_counter += 1
        if problem_counter == max_bad_grades:
            has_failed = True
            break

    problem_name = input()

if has_failed:
    print(f"You need a break, {problem_counter} poor grades.")
else:
    print(f"Average score: {average_score / number_of_problems:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")


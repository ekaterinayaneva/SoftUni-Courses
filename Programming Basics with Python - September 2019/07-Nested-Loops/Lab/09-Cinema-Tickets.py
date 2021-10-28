movie_name = input()

standard_ticket = 0
kid_ticket = 0
student_ticket = 0

total_taken_seats = 0
while movie_name != 'Finish':
    free_seats = int(input())
    counter = 0
    for seats in range(free_seats):
        type_of_ticket = input()
        counter += 1
        if type_of_ticket == 'standard':
            standard_ticket += 1
        elif type_of_ticket == 'kid':
            kid_ticket += 1
        elif type_of_ticket == 'student':
            student_ticket += 1

    total_taken_seats += counter
    taken_percent = free_seats / counter * 100
    print(f"{movie_name} - {taken_percent:.2f}% full.")

    movie_name = input()

print(f"Total tickets: {total_taken_seats}")

student_percent = student_ticket / total_taken_seats * 100
print(f"{student_percent:.2f}% student tickets.")

standard_percent = standard_ticket / total_taken_seats * 100
print(f"{standard_percent:.2f}% student tickets.")

kid_percent = kid_ticket / total_taken_seats * 100
print(f"{kid_percent:.2f}% student tickets.")

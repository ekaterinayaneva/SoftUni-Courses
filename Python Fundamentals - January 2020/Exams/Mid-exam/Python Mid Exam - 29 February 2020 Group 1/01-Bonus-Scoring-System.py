import math

students_count = int(input())
lectures_count = int(input())
bonus = int(input())

max_bonus = 0
student = 0

for i in range(1, students_count + 1):
    student_attendances = int(input())

    total_bonus = student_attendances / lectures_count * (5 + bonus)

    if max_bonus < total_bonus:
        max_bonus = total_bonus
        student = student_attendances


print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {student} lectures.")


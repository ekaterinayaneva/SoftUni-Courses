import math

number_of_people = int(input())
capacity = int(input())

elevator_courses = math.ceil(number_of_people / capacity)

print(elevator_courses)


import sys

number = int(input())

count = 1
biggest_number = -sys.maxsize

while count <= number:
    current_number = int(input())
    count += 1
    if current_number > biggest_number:
        biggest_number = current_number
print(biggest_number)

import sys

number = int(input())

count = 1
min_number = sys.maxsize

while count <= number:
    current_number = int(input())
    count += 1
    if current_number < min_number:
        min_number = current_number

print(min_number)

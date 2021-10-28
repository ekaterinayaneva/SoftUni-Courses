first_employee = int(input())
second_employee = int(input())
third_employee = int(input())

people = int(input())

capacity_per_hour = first_employee + second_employee + third_employee

answered_people = 0
hour = 0

while answered_people < people:

    hour += 1

    if hour % 4 == 0:
        answered_people += 0   #continue
    else:
        answered_people += capacity_per_hour

if answered_people >= people:
    print(f"Time needed: {hour}h.")




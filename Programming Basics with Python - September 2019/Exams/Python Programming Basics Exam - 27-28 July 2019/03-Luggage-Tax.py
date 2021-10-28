width = int(input())
height = int(input())
depth = int(input())
ticket_type = input()


suitcase_size = width * height * depth

luggage_tax = 0

if ticket_type == 'true':
    if 50 < suitcase_size <= 100:
        luggage_tax = 0
    elif 100 < suitcase_size <= 200:
        luggage_tax = 10
    elif 200 < suitcase_size <= 300:
        luggage_tax = 20
elif ticket_type == 'false':
    if 50 < suitcase_size <= 100:
        luggage_tax = 25
    elif 100 < suitcase_size <= 200:
        luggage_tax = 50
    elif 200 < suitcase_size <= 300:
        luggage_tax = 100

print(f"Luggage tax: {luggage_tax:.2f}")

import sys

shortest_time = sys.maxsize
ticket_price = 0
hour = 0
min = 0
flight = ''

command = input()
while command != 'End':
    price = float(input())
    minutes = int(input())

    if minutes < shortest_time:
        shortest_time = minutes

        ticket_price = price * 1.96
        hour = shortest_time // 60
        min = shortest_time % 60
        flight = command

    command = input()

if command == 'End':
    print(f"Ticket found for flight {flight} costs {ticket_price:.2f} leva with {hour}h {min}m stay")







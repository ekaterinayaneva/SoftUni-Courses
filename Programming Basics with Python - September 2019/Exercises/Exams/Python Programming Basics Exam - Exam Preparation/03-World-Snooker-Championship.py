championship_stage = input()
ticket_type = input()
number_of_tickets = int(input())
trophy_photo = input()

ticket_price = 0
photo = 40

if championship_stage == 'Quarter final':
    if ticket_type == 'Standard':
        ticket_price = 55.5
    elif ticket_type == 'Premium':
        ticket_price = 105.2
    elif ticket_type == 'VIP':
        ticket_price = 118.9

elif championship_stage == 'Semi final':
    if ticket_type == 'Standard':
        ticket_price = 75.88
    elif ticket_type == 'Premium':
        ticket_price = 125.22
    elif ticket_type == 'VIP':
        ticket_price = 300.4

elif championship_stage == 'Final':
    if ticket_type == 'Standard':
        ticket_price = 110.1
    elif ticket_type == 'Premium':
        ticket_price = 160.66
    elif ticket_type == 'VIP':
        ticket_price = 400

sum_for_tickets = number_of_tickets * ticket_price

if sum_for_tickets > 4000:
    sum_for_tickets = sum_for_tickets * 0.75
    print(f'{sum_for_tickets:.2f}')

elif sum_for_tickets > 2500:
    sum_for_tickets = sum_for_tickets * 0.9
    if trophy_photo == 'Y':
        trophy_photo = photo * number_of_tickets
        sum_for_tickets += trophy_photo
    print(f'{sum_for_tickets:.2f}')
elif sum_for_tickets < 2500:
    if trophy_photo == 'Y':
        trophy_photo = photo * number_of_tickets
        sum_for_tickets += trophy_photo
        print(f'{sum_for_tickets:.2f}')
    else:
        print(f'{sum_for_tickets:.2f}')



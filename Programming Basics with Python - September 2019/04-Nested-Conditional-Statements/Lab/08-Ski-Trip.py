days = int(input())
type_room = input()
feedback = input()

days = days - 1

disscount = 0
price = 25
if type_room == 'apartment':
    if days < 10:
        disscount = 0.3
    elif 10 <= days <= 15:
        disscount = 0.35
    elif days > 15:
        disscount = 0.5
if type_room == 'president apartment':
    price = 35
    if days < 10:
        disscount = 0.1
    elif 10 <= days <= 15:
        disscount = 0.15
    elif days > 15:
        disscount = 0.2
elif type_room == 'room for one person':
    price = 18


nights_price = days * price
nights_price -= nights_price * disscount

if feedback == 'positive':
    nights_price += nights_price * 0.25
elif feedback == 'negative':
    nights_price -= nights_price * 0.1

print(f'{nights_price:.2f}')

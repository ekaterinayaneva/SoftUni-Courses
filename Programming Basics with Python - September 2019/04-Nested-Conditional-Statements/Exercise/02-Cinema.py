projection = input()
rows = int(input())
columns = int(input())

ticket_price = 0
if projection == 'Premiere':
    ticket_price = 12
elif projection == 'Normal':
    ticket_price = 7.5
elif projection == 'Discount':
    ticket_price = 5

total = rows * columns * ticket_price

print(f'{total:.2f} leva')




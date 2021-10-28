installments = int(input())

count = 1
total_money = 0

while count <= installments:
    amount = float(input())
    if amount < 0:
        print(f'Invalid operation!')
        break

    print(f'Increase: {amount:.2f}')
    total_money += amount
    count += 1

print(f'Total: {total_money:.2f}')


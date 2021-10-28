square_meters = float(input())

price = square_meters * 7.61
sale = 0.18 * price

final_price = price - sale

print(f'The final price is: {final_price:.2f} lv.')
print(f'The discount is: {sale:.2f} lv.')


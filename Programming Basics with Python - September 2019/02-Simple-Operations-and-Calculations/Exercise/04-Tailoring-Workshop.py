table_numbers = int(input())
length = float(input())
width = float(input())

tablecloth = table_numbers * (length + 2 * 0.30) * (width + 2 * 0.30)

table_cover = table_numbers * (length / 2) * (length / 2)

dollar_price = tablecloth * 7 + table_cover * 9

leva_price = dollar_price * 1.85

print(f'{dollar_price:.2f} USD')
print(f'{leva_price:.2f} BGN')



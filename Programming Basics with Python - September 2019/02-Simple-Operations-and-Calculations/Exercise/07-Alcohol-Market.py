whiskey_price = float(input())
beer = float(input())
wine = float(input())
rakia = float(input())
whiskey = float(input())

rakia_price = whiskey_price / 2
wine_price = rakia_price - (0.4 * rakia_price)
beer_price = rakia_price - (0.8 * rakia_price)

beer_sum = beer * beer_price
wine_sum = wine * wine_price
rakia_sum = rakia * rakia_price
whiskey_sum = whiskey * whiskey_price

total_sum = beer_sum + wine_sum + rakia_sum + whiskey_sum

print(f'{total_sum:.2f}')


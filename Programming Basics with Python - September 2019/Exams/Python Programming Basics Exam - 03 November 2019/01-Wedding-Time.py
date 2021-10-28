whiskey_price = float(input())
water_liters = float(input())
wine_liters = float(input())
champagne_liters = float(input())
whiskey_liters = float(input())

champagne_price = whiskey_price * 0.5
wine_price = champagne_price * 0.4
water_price = champagne_price * 0.1

champagne_end_price = champagne_liters * champagne_price
wine_end_price = wine_price * wine_liters
water_end_price = water_price * water_liters
whiskey_end_price = whiskey_price * whiskey_liters

total = champagne_end_price + wine_end_price + water_end_price + whiskey_end_price
print(f'{total:.2f}')

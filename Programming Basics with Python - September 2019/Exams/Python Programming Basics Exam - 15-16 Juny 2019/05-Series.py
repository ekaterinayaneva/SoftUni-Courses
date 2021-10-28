budget = float(input())
number_series = int(input())

price = 0

for series in range(number_series):
    series_name = input()
    series_price = float(input())

    if series_name == 'Thrones':
        series_price = series_price * 0.5
    elif series_name == 'Lucifer':
        series_price = series_price * 0.6
    elif series_name == 'Protector':
        series_price = series_price * 0.7
    elif series_name == 'TotalDrama':
        series_price = series_price * 0.8
    elif series_name == 'Area':
        series_price = series_price * 0.9

    price += series_price


if budget >= price:
    print(f"You bought all the series and left with {budget-price:.2f} lv.")
else:
    print(f"You need {abs(price - budget):.2f} lv. more to buy the series!")



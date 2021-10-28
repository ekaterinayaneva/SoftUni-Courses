days = int(input())
reminder = 0
for day in range(days):
    day_limit = 60 + reminder
    counter = 0
    command = input()
    while True:

        if command == 'Day over':
            print(f"Money left from today: {day_limit:.2f}. You've bought {counter} products.")
            reminder = day_limit
            break

        product_price = float(command)

        if day_limit > product_price:
            day_limit -= product_price
            counter += 1

        if day_limit == product_price:
            counter += 1
            print(f"Daily limit exceeded! You've bought {counter} products.")
            break

        command = input()


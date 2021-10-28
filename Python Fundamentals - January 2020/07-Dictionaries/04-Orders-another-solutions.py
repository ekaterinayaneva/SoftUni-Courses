def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


products = {}
prices = {}

command = input().split()
while command[0] != 'buy':

    for i in range(0, len(command), 3):
        product = command[i]
        price = float(command[i + 1])
        quantity = int(command[i + 2])

        validate_key_existing(products, product)
        products[product] += quantity

        validate_key_existing(prices, product)
        prices[product] = price

    command = input().split()

for key, v in prices.items():
    total_sum = v * products[key]
    print(f"{key} -> {total_sum:.2f}")


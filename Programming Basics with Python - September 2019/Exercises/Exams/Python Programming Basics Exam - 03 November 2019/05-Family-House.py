months = int(input())

electricity = 0
water_bill = 20
internet_bill = 15
total = 0

water = water_bill * months
internet = internet_bill * months

for month in range(months):
    electricity_bill_month = float(input())

    electricity += electricity_bill_month

    other = (electricity_bill_month + water_bill + internet_bill) * 1.2
    total += other

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {total:.2f} lv")
average = (electricity + water + internet + total) / months
print(f"Average: {average:.2f} lv")







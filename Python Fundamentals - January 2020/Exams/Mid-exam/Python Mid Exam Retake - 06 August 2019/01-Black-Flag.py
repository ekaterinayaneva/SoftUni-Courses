plunder_days = int(input())
plunder = int(input())
expected_plunder = int(input())

collected_plunder = 0

for day in range(1, plunder_days + 1):
    collected_plunder += plunder

    if day % 3 == 0:
        collected_plunder += plunder / 2

    if day % 5 == 0:
        collected_plunder *= 0.7

if collected_plunder >= expected_plunder:
    print(f"Ahoy! {collected_plunder:.2f} plunder gained.")
else:
    percentage = collected_plunder / expected_plunder * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")



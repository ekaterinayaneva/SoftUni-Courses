from collections import deque
import math

food_quantity = int(input())

orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    current_order = orders.popleft()
    if food_quantity >= current_order:
        food_quantity -= current_order
    else:
        orders.appendleft(current_order)
        break

if orders:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")
else:
    print(f"Orders complete")


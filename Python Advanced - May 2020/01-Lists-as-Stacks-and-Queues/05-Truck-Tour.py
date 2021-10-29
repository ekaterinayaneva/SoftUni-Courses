from collections import deque

petrol_pumps = int(input())
pumps = deque()
fuel = 0

for i in range(petrol_pumps):
    pump = ([int(x) for x in input().split()])
    pumps.append(pump)


for x in range(petrol_pumps):
    current_pump = pumps.popleft()
    petrol = current_pump[0]
    distance = current_pump[1]

    fuel = petrol - distance

    if fuel > 0:
        print(x)
        break
    else:
        pumps.append(current_pump)

    pumps.append(pumps.popleft())



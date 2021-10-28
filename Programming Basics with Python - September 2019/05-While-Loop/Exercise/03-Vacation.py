money_needed = float(input())
money_available = float(input())

days_count = 0
can_save = True
spend_count = 0

while money_available < money_needed:
    action = input()
    money = float(input())
    days_count += 1
    if action == "spend":
        money_available -= money
        spend_count = spend_count + 1
        if money_available < 0:
            money_available = 0
        if spend_count == 5:
            can_save = False
            break
    elif action == "save":
        money_available += money
        spend_count = 0

if can_save:
    print(f"You saved the money for {days_count} days.")
else:
    print(f"You can't save the money.")
    print(days_count)






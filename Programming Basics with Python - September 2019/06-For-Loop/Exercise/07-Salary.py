tabs_num = int(input())
salary = int(input())

forfeit = 0

for i in range(tabs_num):
    website_name = input()

    if website_name == 'Facebook':
        forfeit = 150
        salary -= forfeit
        if salary <= 0:
            print(f"You have lost your salary.")
            break

    if website_name == 'Instagram':
        forfeit = 100
        salary -= forfeit
        if salary <= 0:
            print(f"You have lost your salary.")
            break

    if website_name == 'Reddit':
        forfeit = 50
        salary -= forfeit
        if salary <= 0:
            print(f"You have lost your salary.")
            break

if salary > 0:
    print(salary)


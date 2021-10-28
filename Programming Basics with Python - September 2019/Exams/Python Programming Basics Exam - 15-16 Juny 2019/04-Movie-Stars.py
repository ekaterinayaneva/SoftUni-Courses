budget = float(input())

actor_name = input()
while True:

    if actor_name == 'ACTION':
        print(f"We are left with {budget:.2f} leva.")
        break

    if len(actor_name) <= 15:
        remuneration = float(input())
        budget -= remuneration
    if len(actor_name) > 15:
        budget = budget * 0.8

    if budget < 0:
        print(f"We need {abs(budget):.2f} leva for our actors.")
        break

    actor_name = input()
    
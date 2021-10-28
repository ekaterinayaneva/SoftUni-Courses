def number(text):
    odd = 0
    even = 0
    for i in text:
        num = int(i)
        if num % 2 == 0:
            even += num
        else:
            odd += num

    return f'Odd sum = {odd}, Even sum = {even}'


text = input()

print(number(text))

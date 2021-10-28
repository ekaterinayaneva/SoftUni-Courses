def percent(n):
    if n == 10:
        print(f'10% [%.........]')
        print(f'Still loading...')

    elif n == 20:
        print(f'20% [%%........]')
        print(f'Still loading...')

    elif n == 30:
        print(f'30% [%%%.......]')
        print(f'Still loading...')

    elif n == 40:
        print(f'40% [%%%%......]')
        print(f'Still loading...')

    elif n == 50:
        print(f'50% [%%%%%.....]')
        print(f'Still loading...')

    elif n == 60:
        print(f'60% [%%%%%%....]')
        print(f'Still loading...')

    elif n == 70:
        print(f'70% [%%%%%%%...]')
        print(f'Still loading...')

    elif n == 80:
        print(f'80% [%%%%%%%%..]')
        print(f'Still loading...')

    elif n == 90:
        print(f'90% [%%%%%%%%%.]')
        print(f'Still loading...')

    elif n == 100:
        print (f'100% Complete!')
        print (f'[%%%%%%%%%%]')

   # return percent(n)


n = int(input())
percent(n)

start_hours = int(input())
start_minutes = int(input())

in_minutes = start_hours * 60 + start_minutes

plus_15_minutes = in_minutes + 15

finale_hour = plus_15_minutes // 60
finale_minutes = plus_15_minutes % 60

if finale_hour > 23:
    finale_hour = finale_hour - 24

if finale_minutes < 10:
    print(f'{finale_hour}:0{finale_minutes}')
else: print(f'{finale_hour}:{finale_minutes}')




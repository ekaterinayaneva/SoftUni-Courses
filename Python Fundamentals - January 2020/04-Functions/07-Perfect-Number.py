def perfect_number(n):
    #sum = []
    result = 0

    for num in range(1, n):
        #divisor = n / num         ne se poluchava
        if n % num == 0:
            result += num
            #sum.append(num)

    return f'We have a perfect number!' if result == n else f"It's not so perfect."


    #return result


n = int(input())
print(perfect_number(n))

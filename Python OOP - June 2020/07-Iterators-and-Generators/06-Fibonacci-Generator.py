def fibonacci():
    previous_sum = 0
    current_sum = 1

    while True:
        yield previous_sum
        previous_sum, current_sum = current_sum, previous_sum + current_sum




generator = fibonacci()

for i in range(5):

    print(next(generator)) 
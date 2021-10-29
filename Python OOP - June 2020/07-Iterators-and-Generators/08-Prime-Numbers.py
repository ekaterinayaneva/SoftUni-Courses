def get_primes(seq):
    for el in seq:
        if el < 2:
            continue
        is_prime = True

        for num in range(2, el):
            if el % num == 0:
                is_prime = False
                break

        if is_prime:
            yield el
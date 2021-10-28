def is_lenght(password):
    return False if 6 <= len(password) <= 10 else True


def is_symbol(password):
    for char in range(password):
        return False if char in range(ord('a'), ord('z') + 1) and \
                         char in range(ord('A'), ord('Z') + 1) and \
                         char in range(ord('0'), ord('9') + 1) \
            else True


def is_digits(password):
    for char in range(password):
        return False if int(char) in range(ord('0'), ord('9') + 1) and \
                         char >= 2 \
            else True


def is_valid(password):
    for char in range(password):
        return True if 6 <= len(password) <= 10 and \
                        char in range(ord('a'), ord('z') + 1) and \
                        range(ord('A'), ord('Z') + 1) and \
                        int(char) in range(ord('0'), ord('9') + 1) \
            else False


def solve(password):
    passwords = [
        [is_lenght, "Password must be between 6 and 10 characters"],
        [is_symbol, "Password must consist only of letters and digits"],
        [is_digits, "Password must have at least 2 digits"],
        [is_valid, "Password is valid"]

    ]
    for fn, result in passwords:
        if fn(password):
            return result

password = input()
print(solve(password))

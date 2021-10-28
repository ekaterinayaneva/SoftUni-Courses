def is_10(number):
    return 10


def is_20(number):
    return 20


def is_30(number):
    return 30


def is_40(number):
    return 40 <= number <= 49


def is_50(number):
    return 50


def is_60(number):
    return 60


def is_70(number):
    return 70


def is_80(number):
    return 80


def is_90(number):
    return 90


def is_100(number):
    return 100


def solve(number):
    percent = [
        [is_10, "10% [%.........]" ],
        [is_10, "Still loading ..."],
        [is_20, "20% [%%........]"],
        [is_20, "Still loading ..."],
        [is_30, "30% [%%%.......]"],
        [is_30, "Still loading ..."],
        [is_40, "40% [%%%%......]"],
        [is_40, "Still loading ..."],
        [is_50, "50% [%%%%%.....]"],
        [is_50, "Still loading ..."],
        [is_60, "60% [%%%%%%....]"],
        [is_60, "Still loading ..."],
        [is_70, "70% [%%%%%%%...]"],
        [is_70, "Still loading ..."],
        [is_80, "80% [%%%%%%%%%..]"],
        [is_80, "Still loading ..."],
        [is_90, "90% [%%%%%%%%%%.]"],
        [is_90, "Still loading ..."],
        [is_100, "100% Complete!"],
        [is_100, "%%%%%%%%%%"],
    ]

    for fn, result in percent:
        if fn(number):
            return result


number = int(input())
print(solve(number))

year = input()
year_as_int = int(year) + 1
year = str(year_as_int)

while True:
    digits_count = len(year)
    unique_count = len(set(year))

    if digits_count == unique_count:
        break

    else:
        year_as_int += 1
        year = year_as_int
        year = str(year_as_int)

print(year)


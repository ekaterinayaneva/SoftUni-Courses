import re

pattern = r"U\$([A-Z][a-z]{2,})U\$P@\$([A-Za-z]{5,}\d+)P@\$"

numbers = int(input())
successful_registrations = 0

for num in range(numbers):
    registration = input()

    match = re.match(pattern, registration)

    if match is None:
        print(f"Invalid username or password")
        continue

    print(f"Registration was successful")
    print(f"Username: {match[1]}, Password: {match[2]}")

    successful_registrations += 1

print(f"Successful registrations: {successful_registrations}")

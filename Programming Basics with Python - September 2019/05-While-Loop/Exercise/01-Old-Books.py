book_name = input()
book_count = int(input())

counter = 1
is_book_found = False

while counter <= book_count:
    current_book = input()

    if current_book == book_name:
        is_book_found = True
        print(f"You checked {counter-1} books and found it.")

        break
    counter += 1

if not is_book_found:
    print(f"The book you search is not here!")
    print(f"You checked {counter-1} books.")

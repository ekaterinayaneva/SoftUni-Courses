books = input().split('&')

instructions = input().split(' | ')

while instructions[0] != 'Done':
    command = instructions[0]

    if command == "Add Book":
        book_name = instructions[1]
        if book_name not in books:
            books.insert(0, book_name)
    elif command == 'Take Book':
        book_name = instructions[1]
        if book_name in books:
            books.remove(book_name)
    elif command == 'Swap Books':
        book_1 = instructions[1]
        book_2 = instructions[2]
        if book_1 in books and book_2 in books:
            i = books.index(book_1)
            x = books.index(book_2)
            books[i], books[x] = books[x], books[i]
    elif command == 'Insert Book':
        book_name = instructions[1]
        books.append(book_name)
    elif command == 'Check Book':
        index = int(instructions[1])
        if 0 <= index < len(books):
            print(books[index])

    instructions = input().split(' | ')


print(', '.join(books))


def string(start, end):
    chars = ''
    for symbols in range(ord(start) +1, ord(end)):
        #print(chr(symbols))

        chars += chr(symbols) + ' '

    return chars


start = input()
end = input()

#string(start,end)

print(string(start, end))


text = input()

cipher = ''

for ch in text:

    letter = ord(ch) + 3

    new_letter = chr(letter)

    cipher += new_letter

print(cipher)





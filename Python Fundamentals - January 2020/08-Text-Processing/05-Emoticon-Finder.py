text = input()

for i in range(len(text)):
    if text[i] == ':':
        if i + 1 < len(text) and i + 1 != ' ':
            print(f':{text[i + 1]}')

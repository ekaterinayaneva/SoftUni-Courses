string = input()

list = []

for i in range(len(string)):
    if len(string) < len(string[i + 1]):
        break

    if not string[i] == string[i+1]:
            #continue
        #else:
        list.append(string[i])

  #  i += 1

print(''.join(list))





text = input().split(' ')

a = map(lambda c: c if c.isalnum() else '', text)
print(a)
#list = list(set(text))
#print(list)
#text[1], text[]
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
to_int = 0
for word in text:
    for i in word:
        if i in digits:
            to_int += i
          #  print(to_int)

   # to_int = int(word[0] + word[1])
  #  first_letter = chr(to_int)
   # print(to_int)

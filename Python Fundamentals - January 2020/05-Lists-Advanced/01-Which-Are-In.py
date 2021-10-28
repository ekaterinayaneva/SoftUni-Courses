special_words = input().split(', ')
words = input()#.split(', ')

unique_words = [word for word in special_words if word in words]

print(unique_words)

n = int(input())
username_set = set()

for i in range(n):
    username = input()

    username_set.add(username)

#for username in username_set:
 #   print(username)

#print('\n'.join(username_set))

[print(x) for x in username_set]


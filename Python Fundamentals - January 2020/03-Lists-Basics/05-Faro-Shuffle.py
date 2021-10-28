cards_str = input().split(' ')
faro_shuffles = int(input())

#cards = []

#for i in cards_str:
#    cards.append(i)

result = [] * faro_shuffles

for card in range(len(cards_str)):
    index = card % 2
    result[index] = cards_str[card]

    print(result)

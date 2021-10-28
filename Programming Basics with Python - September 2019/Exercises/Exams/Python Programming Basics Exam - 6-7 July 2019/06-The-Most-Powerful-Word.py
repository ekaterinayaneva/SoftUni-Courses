import math
word = input()

vowel = 'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'
winner_sum = 0
winner_word = ''
word_sum = 0

while word != "End of words":
    sum = 0
    for letter in word:
        ascii_value = ord(letter)
        sum += ascii_value

        if word[0] in vowel:
            word_sum = sum * len(word)
        else:
            word_sum = math.floor(sum / len(word))

    if word_sum > winner_sum:
        winner_sum = word_sum
        winner_word = word

    word = input()

print(f"The most powerful word is {winner_word} - {winner_sum}")


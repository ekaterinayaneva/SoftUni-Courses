import re

text_input = input()

words_found = 0
mirror_words = {}

pattern = r"(@|#)([A-z]{3,})\1((@|#)([A-z]{3,})\1)"

matches = re.findall(pattern, text_input)
#print(matches)

for match in matches:
    words_found += 1

    rev_group_2 = match[4]
    rev_group_2 = rev_group_2[::-1]

    if match[1] == rev_group_2:
        word = match[1]
        mirr_word = match[4]
        mirror_words[word] = mirr_word

if words_found >= 1:
    print(f"{words_found} word pairs found!")
else:
    print(f"No word pairs found!")

if not mirror_words:
    print(f"No mirror words!")
else:
    print(f'The mirror words are:')
    print(', '.join('{} <=> {}'.format(k, v) for k,v in mirror_words.items()))



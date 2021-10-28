import re

string_input = input()

emojis = []
cool_threshold = 1
emoji_count = 0
sum_ch_emoji = 0


pattern_emojis = r"([**|::]{2})([A-Z][a-z]{2,})\1"
pattern_numbers = r"\d"


emoji_matches = re.finditer(pattern_emojis, string_input)
for emoji in emoji_matches:
    emojis.append(emoji[0])
    emoji_count += 1


number_matches = re.findall(pattern_numbers, string_input)
for num in number_matches:
    cool_threshold *= int(num)


print(f'Cool threshold: {cool_threshold}')
print(f'{emoji_count} emojis found in the text. The cool ones are:')


for emoji in emojis:
    sum_ch_emoji = 0
    for ch in emoji:
        if ch == ':' or ch == '*':
            continue
        sum_ch_emoji += ord(ch)
    if sum_ch_emoji > cool_threshold:
        print(emoji)


def get_repeating_DNA(string):
    result = []

    for inx in range(len(string) - 10):
        substring = string[inx:inx+10]

        if substring in string[inx+1:] and substring not in result:
            result.append(substring)

    return result




test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)

test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)

test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)

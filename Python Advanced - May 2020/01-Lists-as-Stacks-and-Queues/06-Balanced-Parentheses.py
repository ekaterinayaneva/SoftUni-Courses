brackets = [i for i in input()]

new_brackets = []
breaked = False

for i in brackets:
    if i == "(":
        new_brackets.append(i)
    elif i == "{":
        new_brackets.append(i)
    elif i == "[":
        new_brackets.append(i)
    elif i == ")":
        if "(" not in new_brackets or new_brackets.pop() != "(":
            breaked = True
            break
    elif i == "]":
        if "[" not in new_brackets or new_brackets.pop() != "[":
            breaked = True
            break
    elif i == "}":
        if "{" not in new_brackets or new_brackets.pop() != "{":
            breaked = True
            break
        
if not breaked:
    print("YES")
else:
    print("NO")








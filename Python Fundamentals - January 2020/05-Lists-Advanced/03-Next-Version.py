prog_version = list(map(int, input().split('.')))

prog_version[2] += 1

if prog_version[2] == 10:
    prog_version[2] = 0
    prog_version[1] += 1

if prog_version[1] == 10:
    prog_version[1] = 0
    prog_version[0] += 1

print('.' .join(map(str, prog_version)))


#           ili

prog_version = int(input().replace('.' , ''))
prog_version += 1

print('.'.join(list(str(prog_version))))

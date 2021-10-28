concert = {}
playing_time = {}
total_time = 0

while True:
    args = input()

    if args == 'start of concert':
        special_band_name = input()
        break

    command = args.split("; ")

    if command[0] == 'Add':
        band_name = command[1]
        members = command[2].split(', ')

        if band_name not in concert:
            concert[band_name] = []
        for member in members:
            if member not in concert[band_name]:
                concert[band_name].append(member)
                #print(concert)

    elif command[0] == 'Play':
        band_name = command[1]
        time = int(command[2])

        if band_name not in playing_time:
            playing_time[band_name] = time
        else:
            playing_time[band_name] += time

        total_time += time


print(f'Total time: {total_time}')

#playing_time = dict(sorted(playing_time.items(), key=lambda m: (-len(m[0]), m[1])))

for band, time in sorted(playing_time.items(), key=lambda m: (-(m[1]), m[1])):
    print(f'{band} -> {time}')

if special_band_name in concert:
    print(f'{special_band_name}')
    for member in concert[special_band_name]:
        print(f'=> {member}')


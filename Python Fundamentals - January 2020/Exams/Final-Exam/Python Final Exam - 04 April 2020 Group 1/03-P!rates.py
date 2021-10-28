args = input().split('||')

city_population_gold = {}

while args[0] != 'Sail':
    city = args[0]
    population = int(args[1])
    gold = int(args[2])

    if city not in city_population_gold:
        city_population_gold[city] = []
        city_population_gold[city].append(population)
        city_population_gold[city].append(gold)
    else:
        city_population_gold[city][0] += population
        city_population_gold[city][1] += gold

    args = input().split('||')


command = input().split('=>')

while command[0] != 'End':

    if command[0] == 'Plunder':
        town = command[1]
        people = int(command[2])
        gold = int(command[3])

        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        if town in city_population_gold:

            city_population_gold[town][1] -= gold
            city_population_gold[town][0] -= people

            if city_population_gold[town][0] <= 0:
                print(f"{town} has been wiped off the map!")
                del city_population_gold[town]

            elif city_population_gold[town][1] <= 0:
                print(f"{town} has been wiped off the map!")
                del city_population_gold[town]

    elif command[0] == 'Prosper':
        town = command[1]
        gold = int(command[2])

        if gold < 0:
            print(f"Gold added cannot be a negative number!")
            #continue

        else:
            city_population_gold[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {city_population_gold[town][1]} gold.")


    command = input().split('=>')

print(f'Ahoy, Captain! There are {len(city_population_gold)} wealthy settlements to go to:')

for town, value in sorted(city_population_gold.items(), key=lambda v: (-v[1][1], v[0])):
    print(f'{town} -> Population: {value[0]} citizens, Gold: {value[1]} kg')

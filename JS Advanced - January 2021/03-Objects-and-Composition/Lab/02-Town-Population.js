function townPopulation(townsArray) {
    const towns = {}

    for (let townAsString of townsArray) {
        let [name, population] = townAsString.split(' <-> ')
        population = Number(population)

        if (towns[name] != undefined) {
            population += towns[name]
        }
        towns[name] = population
    }

    for (let [name, population] of Object.entries(towns)) {
        console.log(`${name} : ${population}`)
    }
}





townPopulation(['Istanbul <-> 100000',
    'Honk Kong <-> 2100004',
    'Jerusalem <-> 2352344',
    'Mexico City <-> 23401925',
    'Istanbul <-> 1000']
)
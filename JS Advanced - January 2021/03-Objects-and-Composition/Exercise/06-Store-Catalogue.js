function solve(input) {
    const dict = {}
    let result = []

    while (input.length) {
        let [product, price] = input.shift().split(' : ')
        price = Number(price)
        let firstLetter = product[0]

        if (!dict[firstLetter]) {
            dict[firstLetter] = []
        }

        dict[firstLetter].push({product, price})
    }

    Object.entries(dict).sort((a, b) => a[0].localeCompare(b[0])).forEach(entry => {
        let values = entry[1]
        .sort((a, b) => (a.product).localeCompare(b.product))
        .map(product => `  ${product.product}: ${product.price}`)
        .join('\n')

        result.push(`${entry[0]}\n${values}`)
    });

    return result.join('\n')
}


console.log(solve(['Appricot : 20.4',
    'Fridge : 1500',
    'TV : 1499',
    'Deodorant : 10',
    'Boiler : 300',
    'Apple : 1.25',
    'Anti-Bug Spray : 15',
    'T-Shirt : 10']
))
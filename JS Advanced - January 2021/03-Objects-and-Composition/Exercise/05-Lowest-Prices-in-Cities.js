function solve(input) {
    let lowest_price = {}

    while (input.length) {
        let delimeter = input.shift()
        let [town, product, price] = delimeter.split(' | ')
        price = Number(price)

        if (!lowest_price[product]) {
            lowest_price[product] = {town, price}
        } else {
            lowest_price[product] = lowest_price[product].price  <= price ? lowest_price[product] : {town, price}
        }
    }
    let result = []
    for (const product in lowest_price) {
        result.push(`${product} -> ${lowest_price[product].price} (${lowest_price[product].town})`)
    }

    return result.join('\n')
}


console.log(solve(['Sample Town | Sample Product | 1000',
    'Sample Town | Orange | 2',
    'Sample Town | Peach | 1',
    'Sofia | Orange | 3',
    'Sofia | Peach | 2',
    'New York | Sample Product | 1000.1',
    'New York | Burger | 10']
))

function solve(arr) {

    let quantityMap = new Map()
    let bottlesMap = new Map()
    for (let token of arr) {

        let [fruit, quantity] = token.split(' => ')

        if (quantityMap.has(fruit)) {
            quantityMap.set(fruit, quantityMap.get(fruit) + Number(quantity))
        } else {
            quantityMap.set(fruit, Number(quantity))
        }

        if (quantityMap.get(fruit) >= 1000) {
            let bottles = Math.floor(quantityMap.get(fruit) / 1000)

            quantityMap.set(fruit, quantityMap.get(fruit) - bottles * 1000)

            if (bottlesMap.has(fruit)) {
                bottlesMap.set(fruit, bottlesMap.get(fruit) + bottles)
            } else {
                bottlesMap.set(fruit, bottles)
            }
        }
    }

    bottlesMap.forEach((b, f) => {
        console.log(`${f} => ${b}`)
    })

}


solve(['Orange => 2000',
    'Peach => 1432',
    'Banana => 450',
    'Peach => 600',
    'Strawberry => 549']
)


solve(['Kiwi => 234',
    'Pear => 2345',
    'Watermelon => 3456',
    'Kiwi => 4567',
    'Pear => 5678',
    'Watermelon => 6789']
)
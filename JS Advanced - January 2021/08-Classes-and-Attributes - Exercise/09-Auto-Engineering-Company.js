function solve(arr) {
    let split = []
    
    for (let i = 0; i< arr.length; i++) {
        split.push(arr[i].split(' | '))
    }

    let storage = new Map

    for (let i = 0; i< split.length; i++) {
        let cars = split[i]

        let [brand, model, quantity] = cars

        if (!storage.has(brand)) {
            storage.set(brand, new Map())
        }

        if (!storage.get(brand).has(model)) {
            storage.get(brand).set(model, 0)
        }

        let value = Number(storage.get(brand).get(model))
        storage.get(brand).set(model, value + Number(quantity))
    }
    resultStr = []
    for ([brand, model] of storage.entries()) {
        res = `${brand}\n`
        for (let [name, quantity] of model.entries()) {
            res += `###${name} -> ${quantity}\n`
        }

        resultStr.push(res.trim())
    }

return resultStr.join('\n')
}



console.log(solve(['Audi | Q7 | 1000',
'Audi | Q6 | 100',
'BMW | X5 | 1000',
'BMW | X6 | 100',
'Citroen | C4 | 123',
'Volga | GAZ-24 | 1000000',
'Lada | Niva | 1000000',
'Lada | Jigula | 1000000',
'Citroen | C4 | 22',
'Citroen | C5 | 10']))

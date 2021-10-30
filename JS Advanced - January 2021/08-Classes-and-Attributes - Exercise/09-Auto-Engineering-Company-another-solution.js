function solve(input) {
    let output = {};

    input.forEach(entry => {
        let [carBrand, carModel, producedCars] = entry.split(' | ');
        if (!output.hasOwnProperty(carBrand)) {
            output[carBrand] = {};
        }
        if (!output[carBrand].hasOwnProperty(carModel)) {
            output[carBrand][carModel] = 0;
        }
        output[carBrand][carModel] += Number(producedCars);
    })

    Object.keys(output).forEach(key => {
        console.log(key);
        Object.keys(output[key]).forEach(model => {
            console.log(`###${model} -> ${output[key][model]}`);
        })
    })
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
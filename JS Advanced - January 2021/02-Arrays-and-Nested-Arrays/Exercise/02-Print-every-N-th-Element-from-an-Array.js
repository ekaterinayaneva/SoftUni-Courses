function solve(numbers, step) {
    const result = []

    for (let i = 0; i < numbers.length ; i += step) {
        result.push(numbers[i])
    }

    return result
}

    //for (let i = 0; i < numbers.length ; i ++) {                        // podobno reshenie 
        //if (i % step == 0)
            //result.push(numbers[i])
    //}
    //return result
//}



//const solve = (numbers, step) => numbers.filter((elent, index) => {return index % step === 0})        // drugo reshenie


console.log(solve(['5',
    '20',
    '31',
    '4',
    '20'],
    2
))


console.log(solve(['dsa',
    'asd',
    'test',
    'tset'],
    2
))


console.log(solve(['1',
    '2',
    '3',
    '4',
    '5'],
    6
))
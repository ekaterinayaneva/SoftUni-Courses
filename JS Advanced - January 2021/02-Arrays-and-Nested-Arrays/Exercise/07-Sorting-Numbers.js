function solve(numbers) {
    let result = []

    numbers.sort((a,b) => a-b)

    while (numbers.length) {
        result.push(numbers.shift())
        result.push(numbers.pop())
    }

    return result.filter(num => num != undefined)        // v sluchai che imame necheten broi chisla, togava shte poluchim undefined, 
                                                        //zashtoto v while izvurshvame dve operacii
}


console.log(solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]))

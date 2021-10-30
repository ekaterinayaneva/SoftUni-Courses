function mathOperations(num1, num2, operator) {
    const operations = {
        '+': (num1, num2) => num1 + num2,
        '-': (num1, num2) => num1 - num2,
        '*': (num1, num2) => num1 * num2,
        '/': (num1, num2) => num1 / num2,
        '**': (num1, num2) => num1 ** num2,
        '%': (num1, num2) => num1 % num2,
        
    }

    console.log(operations[operator] (num1, num2))
}


mathOperations(5, 6, '+')
mathOperations(3, 5.5, '*')

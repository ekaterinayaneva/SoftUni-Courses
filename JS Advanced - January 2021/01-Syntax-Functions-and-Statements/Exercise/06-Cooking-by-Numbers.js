function solve(num, ...params) {
    let number = +num
    const result = []

    for (let i = 0; i < params.length; i++ ) {
        switch (params[i]) {
            case 'chop':
                number /= 2
                result.push(number)
                break;
            case 'dice':
                number = Math.sqrt(number)
                result.push(number)
                break;
            case 'spice':
                number++
                result.push(number)
                break;
            case 'bake':
                number *= 3
                result.push(number)
                break;
            case 'fillet':
                number -= number * 0.2
                result.push(number)
                break;
        }
    }

    return result.join('\n')
}


console.log(solve('32', 'chop', 'chop', 'chop', 'chop', 'chop'))
console.log(solve('9', 'dice', 'spice', 'chop', 'bake', 'fillet'))
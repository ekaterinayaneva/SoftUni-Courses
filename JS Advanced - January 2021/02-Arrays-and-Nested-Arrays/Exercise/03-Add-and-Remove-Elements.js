function solve(commands) {
    const result = [];
    let number = 1;

    for (const command of commands) {
        if (command == 'add') {
            result.push(number)
        } else if (command == 'remove') {
            result.pop()
        }

        number++
    }

    return result.length == 0 ? 'Empty' : result.join('\n');
}


console.log(solve(['add',
    'add',
    'add',
    'add']
))


console.log(solve(['add',
    'add',
    'remove',
    'add',
    'add']
))


console.log(solve(['remove',
    'remove',
    'remove']
))

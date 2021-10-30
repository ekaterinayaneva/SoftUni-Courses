function solve(input) {
    let result = [];
    let num = 0;

    for (let i = 0; i < input.length; i++) {
        num++;
        if (input[i] === 'add') {
            result.push(num);
        } else if (input[i] === 'remove') {
            result.pop(i);
        }
    }

    return result.length == 0 ? 'Empty' : result.join(' ')
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
function solve(inputStr) {
    const result = {};

    for (let i = 0; i < inputStr.length; i += 2) {
        result[inputStr[i]] = Number(inputStr[i + 1]);
    }
    return result;
}


//console.log(solve(['Yoghurt', '48', 'Rise', '138', 'Apple', '52']))

console.log(solve(['Potato', '93', 'Skyr', '63', 'Cucumber', '18', 'Milk', '42']))
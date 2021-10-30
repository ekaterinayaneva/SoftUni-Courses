function solve(numbers) {
    return numbers
    .filter((a, x) => x % 2 !== 0)                // x moje da naimenuvame po drug nachin, nqma vruzka s map x
    .map(x => x* 2)
    .reverse()
    .join(' ')
}


console.log(solve([10, 15, 20, 25]))
console.log(solve([3, 0, 10, 4, 7, 3]))

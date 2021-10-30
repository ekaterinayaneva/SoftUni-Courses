function solve(n, k) {
    let result = [1]

    for (let i = 1; i < n; i++) {
        let startIndex = Math.max(0, i - k)
        let number = result
            .slice(startIndex, startIndex + k)
            .reduce((acc, el) => acc + el, 0)

        result.push(number)
    }

    return result.join()
}


console.log(solve(6, 3))
console.log(solve(8, 2))

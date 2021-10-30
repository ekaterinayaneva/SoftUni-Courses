function solve(number) {
    const numTostr = number.toString()
    let isSame = true
    let sum = 0

    for (let i = 0; i < numTostr.length; i++) {
        current = numTostr[i]
        next = numTostr[i + 1]

        if (current !== next && next != undefined) {
            isSame = false
        }

        sum += Number(current)
    }

    console.log(isSame)
    console.log(sum)

}


solve(2222222)
solve(1234)
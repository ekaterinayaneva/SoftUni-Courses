function aggrEl(input) {
    let sum = 0
    let reciproc = 0
    let concat = ''

    for (let i = 0; i < input.length; i++ ) {
        sum += input[i]
        reciproc += 1/ input[i]
        concat += input[i]
    }

    console.log(sum)
    console.log(reciproc)
    console.log(concat)
}


aggrEl([1, 2, 3])
aggrEl([2, 4, 8, 16])




// ANOTHER SOLUTION
// function aggrEl(input) {
//     console.log(input.reduce((acc, c) => acc + c, 0))
//     console.log(input.reduce((acc, c) => acc + 1/c, 0))
//     console.log(input.reduce((acc, c) => acc + c, ''))
// }


// aggrEl([1, 2, 3])
// aggrEl([2, 4, 8, 16])
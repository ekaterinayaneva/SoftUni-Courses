function stringLength(...params) {
    let total = params.reduce((a, c) => a + c.length, 0)
    console.log(total)
    console.log(Math.floor(total / params.length))
}


stringLength('chocolate', 'ice cream', 'cake')
stringLength('pasta', '5', '22.3')


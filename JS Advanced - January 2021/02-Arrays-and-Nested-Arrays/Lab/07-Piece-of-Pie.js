function solve(pies, startFlavor, endFlavor) {
    const result = [pies, startFlavor, endFlavor]

    const start = indexof(startFlavor)
    const end = indexof(endFlavor) 

    result = result.slice(start, end)
    return result
}


console.log(solve(['Pumpkin Pie',
    'Key Lime Pie',
    'Cherry Pie',
    'Lemon Meringue Pie',
    'Sugar Cream Pie'],
    'Key Lime Pie',
    'Lemon Meringue Pie'
))


console.log(solve(['Apple Crisp',
    'Mississippi Mud Pie',
    'Pot Pie',
    'Steak and Cheese Pie',
    'Butter Chicken Pie',
    'Smoked Fish Pie'],
    'Pot Pie',
    'Smoked Fish Pie'
))
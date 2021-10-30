function solve(strArr) {
    const first = Number([...strArr].shift())    // po tozi nachin pravim plitko kopie na masiva i ne go promenqme
    const last = Number([...strArr].pop())

    return first + last
}


console.log(solve(['20', '30', '40']))
console.log(solve(['5', '10']))

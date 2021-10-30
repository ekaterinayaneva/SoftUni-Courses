function solve(arr) {

    let rowSums = []
    let colSums = []

    //Намираме сумите на всички редове
    for (let i = 0; i < arr.length; i++) {
        let row = arr[i];
        let sum = row.reduce((result, curr) => (result + curr), 0);
        rowSums.push(sum);
    }


    //Намираме сумите на всички колони
    for (let i = 0; i < arr.length; i++) {
        let newRow = []
        for (let y = 0; y < arr.length; y++) {
            newRow.push(arr[y][i])
        }

        let sum = newRow.reduce((result, curr) => (result + curr), 0);
        colSums.push(sum);
    }

    //Събираме резултатите в един масив и проверяваме дали всички елементи са еднакви

    for (let i = 0; i < rowSums.length; i++) {
        if (rowSums[i] !== colSums[i] || rowSums[0] !== rowSums[i]) {
            return false;
        }
    }

    return true;
}


console.log(solve([[11, 32, 45],
    [21, 0, 1],
    [21, 1, 1]]
   
))

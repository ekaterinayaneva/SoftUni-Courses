function solve(arr) {
 
    //Намираме сумите на всички редове
    let rowSums = arr.map((el) => el.reduce((a, b) => a + b), 0);

 
 
    //Намираме сумите на всички колони
    let colSums = arr[0].map((_, col) => arr.map((row) => row[col])).map(row => row.reduce((a, b) => a + b));

 
    //Събираме резултатите в един масив и проверяваме дали всички елементи са еднакви
    return rowSums.concat(colSums).every((el, i, arr) => el === arr[0]);
 
}


console.log(solve([[4, 5, 6],
    [6, 5, 4],
    [5, 5, 5]]
    ))
    
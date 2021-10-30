function solve(...params) {
    let types = {};
    for(const param of params) {
        let type = typeof param;
        if(!types.hasOwnProperty(type)) {
            types[type] = 0;
        }
 
        types[type]++;
        console.log(`${type}: ${param}`);
    }
 
    let sorted = [];
 
    for(const type in types) {
        sorted.push([type, types[type]]);
    }
 
    sorted.sort((a, b) => b[1] - a[1]);
    for(const type of sorted) {
        console.log(`${type[0]} = ${type[1]}`);
    }
}


solve('cat', 42, function () { console.log('Hello world!'); });

function solve(){
    let result = [];
    let count = {};

    [...arguments].forEach(arg => {
        let value = arg;
        let type = typeof value;

        result.push({type, value});

        if(!count[type]){
            count[type] = 0;
        }

        count[type]++;
    });
    
    result.forEach(res => {
        console.log(`${res.type}: ${res.value}`);
    });

    let sortedCount = Object.entries(count).sort((a,b) => b[1] - a[1]);
    sortedCount.forEach(elem => console.log(`${elem[0]} = ${elem[1]}`));
}

solve('cat', 42, function () { console.log('Hello world!'); });
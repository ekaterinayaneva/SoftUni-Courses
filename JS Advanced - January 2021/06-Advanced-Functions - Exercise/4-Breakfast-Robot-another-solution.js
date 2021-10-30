function solution() {
    function restock(input) {
        //⦁   restock <microelement> <quantity> - increases the stored quantity of the given microelement
        let microelement = input[0].toLowerCase();
        let quantity = Number(input[1]);
        microelements[microelement] += Number(quantity);
        return 'Success';
    }
 
    function prepare(input) {
        //⦁   prepare <recipe> <quantity> - uses the available ingredients to prepare the given meal
        let recipe = input[0].toLowerCase();
        let quantity = Number(input[1]);
        let result = '';
 
        if (quantity * recipes[recipe].protein > microelements.protein) {
            result = 'Error: not enough protein in stock';
        } else if (quantity * recipes[recipe].protein < microelements.protein) {
            result = 'Success';
            microelements.protein -= quantity * recipes[recipe].protein;
 
        }
 
    }
 
    function report(input) {
 
    }
 
 
 
 
    let microelements = {
        protein: 0,
        carbohydrate: 0,
        fat: 0,
        flavour: 0
    };
 
    let recipes = {
        apple: {
            protein: 0,
            carbohydrate: 1,
            fat: 0,
            flavour: 2
        },
        lemonade: {
            protein: 0,
            carbohydrate: 10,
            fat: 0,
            flavour: 20
        },
        burger: {
            protein: 0,
            carbohydrate: 5,
            fat: 7,
            flavour: 3
        },
        eggs: {
            protein: 5,
            carbohydrate: 0,
            fat: 1,
            flavour: 1
        },
        turkey: {
            protein: 10,
            carbohydrate: 10,
            fat: 10,
            flavour: 10
        }
    };
 
 
    return function (command) {
        command = command.split(' ');
        let action = command.shift();
        if (action === 'restock') {
            return restock(command);
        } else if (action === 'prepare') {
            return prepare(command);
        } else {
            return report(command);
        }
 
    };
}


let manager = solution();

console.log(manager("restock flavour 10"));
console.log(manager("restock carbohydrate 10"));
console.log(manager("prepare apple 1"));
console.log(manager("restock fat 10"));
console.log(manager("prepare burger 1"));
console.log(manager("report"));

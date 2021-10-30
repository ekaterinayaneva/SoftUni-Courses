function solution() {
    const ingredientsInStock = createIngredientsObject(0, 0, 0, 0)
    
    
    const recipes = {
        apple: createIngredientsObject(0, 1, 0, 2),
        lemonade: createIngredientsObject(0, 10, 0, 20),
        burger: createIngredientsObject(0, 5, 7, 3),
        eggs: createIngredientsObject(5, 0, 1, 1),
        turkey: createIngredientsObject(10, 10, 10, 10),
    }
    
    const commands = {
        restock: (ingredient, qty) => {
            ingredientsInStock[ingredient] += qty;
            return "Success";
        },
        report: () => `protein=${ingredientsInStock["protein"]} carbohydrate=${ingredientsInStock["carbohydrate"]} fat=${ingredientsInStock["fat"]} flavour=${ingredientsInStock["flavour"]}`,
        prepare: function (item, qty) {
            var recipe = recipes[item];
            
            for (const key in recipe) {
                if (recipe[key] * qty > ingredientsInStock[key]) {               
                    return `Error: not enough ${key} in stock`;
                }
            }
            
            for (const key in recipe) {
                ingredientsInStock[key] -= recipe[key] * qty;
            }
            return ("Success");
        }
    }
    
    return work;
    
    function createIngredientsObject(qty, qty2, qty3, qty4) {
        return {
            protein: qty,
            carbohydrate: qty2,
            fat: qty3,
            flavour: qty4
        }
    }
    function work(commandArr) {
        var [command, item, qty] = commandArr.split(' ');

        return commands[command](item, Number(qty));
    }
}


let manager = solution();
// manager("restock flavour 50");  // Success
// manager("prepare lemonade 4");  


// console.log(manager("restock flavour 10"));
// console.log(manager("restock carbohydrate 10"));
// console.log(manager("prepare apple 1"));
// console.log(manager("restock fat 10"));
// console.log(manager("prepare burger 1"));
// console.log(manager("report"));


console.log(manager("prepare turkey 1"));
console.log(manager("restock protein 10"));
console.log(manager("prepare turkey 1"));
console.log(manager("restock carbohydrate 10"));
console.log(manager("prepare turkey 1"));
console.log(manager("restock fat 10"));
console.log(manager("prepare turkey 1"));
console.log(manager("restock flavour 10"));
console.log(manager("prepare turkey 1"));
console.log(manager("report"));

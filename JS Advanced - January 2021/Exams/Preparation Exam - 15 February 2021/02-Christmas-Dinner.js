class ChristmasDinner {
    constructor(budget) {
        this.budget = budget
        this.dishes = []
        this.products = []
        this.guests = {}
    }

    set budget(value) {
        if (value < 0) {
            throw new Error("The budget cannot be a negative number")
        }

        this._budget = value
    }

    get budget() {
        return this._budget
    }


    shopping([type, price]) {                                     // shopping([product])  =>  shopping([type, price])
        if (this.budget < price) {
            throw new Error("Not enough money to buy this product")
        }

        this.products.push(type)
        this.budget -= price
        return `You have successfully bought ${type}!`
    }


    recipes({ recipeName, productsList }) {                                        //  { recipeName: string, productsList: [array of strings] }
        if (productsList.some(p => this.products.includes(p) == false)) {         //   namirame dali imame suvpadenie na konkreten produkt ot productsList v products
            throw new Error("We do not have this product")
        }

        this.dishes.push({ recipeName, productsList })               // this.dishes = []    masiv/array dobavq obekti v sebe si
        return `${recipeName} has been successfully cooked!`
    }

    inviteGuests(name, dish) {
        if (this.dishes.some(d => d.recipeName == dish) == false) {             // namirane dali v obekta/masiva dishes ima konkretnoto qstie dish
            throw new Error("We do not have this dish")
        }

        if (this.guests.hasOwnProperty(name)) {                             // namirame dali v obekta ima konkretno ime (suzdadeno property s tova ime)
            throw new Error("This guest has already been invited")
        }

        this.guests[name] = dish                                // this.guests = {}    obekt dobavq v sebe si
        return `You have successfully invited ${name}!`
    }

    showAttendance() {
        let result = []

        // vzimame masiva s negovite kluchove i stoinosti, s forEach za vsqko edno entry go destrukturirame po kluch i stoinost
        Object.entries(this.guests).forEach(([guestName, dish]) => {            
            result.push(`${guestName} will eat ${dish}, which consists of ${this.dishes.find(d => d.recipeName == dish).productsList.join(', ')}`)
        });                                                               // namirame sustavkite na qstieto, koito sa v productsList

        return result.join('\n')
    }
}



let dinner = new ChristmasDinner(300);

dinner.shopping(['Salt', 1]);
dinner.shopping(['Beans', 3]);
dinner.shopping(['Cabbage', 4]);
dinner.shopping(['Rice', 2]);
dinner.shopping(['Savory', 1]);
dinner.shopping(['Peppers', 1]);
dinner.shopping(['Fruits', 40]);
dinner.shopping(['Honey', 10]);

dinner.recipes({
    recipeName: 'Oshav',
    productsList: ['Fruits', 'Honey']
});
dinner.recipes({
    recipeName: 'Folded cabbage leaves filled with rice',
    productsList: ['Cabbage', 'Rice', 'Salt', 'Savory']
});
dinner.recipes({
    recipeName: 'Peppers filled with beans',
    productsList: ['Beans', 'Peppers', 'Salt']
});

dinner.inviteGuests('Ivan', 'Oshav');
dinner.inviteGuests('Petar', 'Folded cabbage leaves filled with rice');
dinner.inviteGuests('Georgi', 'Peppers filled with beans');

console.log(dinner.showAttendance());

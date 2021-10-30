const { assert, expect } = require("chai")
const { describe } = require("mocha")

let pizzUni = {
    makeAnOrder: function (obj) {

        if (!obj.orderedPizza) {
            throw new Error('You must order at least 1 Pizza to finish the order.');
        } else {
            let result = `You just ordered ${obj.orderedPizza}`
            if (obj.orderedDrink) {
                result += ` and ${obj.orderedDrink}.`
            }
            return result;
        }
    },

    getRemainingWork: function (statusArr) {

        const remainingArr = statusArr.filter(s => s.status != 'ready');

        if (remainingArr.length > 0) {

            let pizzaNames = remainingArr.map(p => p.pizzaName).join(', ')
            let pizzasLeft = `The following pizzas are still preparing: ${pizzaNames}.`

            return pizzasLeft;
        } else {
            return 'All orders are complete!'
        }

    },

    orderType: function (totalSum, typeOfOrder) {
        if (typeOfOrder === 'Carry Out') {
            totalSum -= totalSum * 0.1;

            return totalSum;
        } else if (typeOfOrder === 'Delivery') {

            return totalSum;
        }
    }
}


describe('pizzUni', function () {
    it('makeAnOrder', function () {
        let pizza = { orderedPizza: 'pizza', orderedDrink: 'drink' }
        let pizza1 = { orderedPizza: 'pizza' }
        let pizza2 = { orderedDrink: 'drink' }
        let pizza3 = {}

        assert.equal(pizzUni.makeAnOrder(pizza), `You just ordered ${pizza.orderedPizza} and ${pizza.orderedDrink}.`)
        assert.equal(pizzUni.makeAnOrder(pizza1), `You just ordered ${pizza.orderedPizza}`)

        assert.throw(() => pizzUni.makeAnOrder(pizza2), 'You must order at least 1 Pizza to finish the order.')
        assert.throw(() => pizzUni.makeAnOrder(pizza3), 'You must order at least 1 Pizza to finish the order.')
    })

    it('getRemainingWork', function () {
        let statusArr = [
            { pizzaName: 'pizza', status: 'ready' },
            { pizzaName: 'pizza1', status: 'ready' },
            { pizzaName: 'pizza2', status: 'preparing' },
            { pizzaName: 'pizza3', status: 'preparing' }
        ]

        let statusArr1 = [
            { pizzaName: 'pizza', status: 'ready' },
            { pizzaName: 'pizza1', status: 'ready' },
        ]

        let statusArr2 = [
            { pizzaName: 'pizza2', status: 'preparing' },
            { pizzaName: 'pizza3', status: 'preparing' }
        ]

        assert.equal(pizzUni.getRemainingWork(statusArr), `The following pizzas are still preparing: pizza2, pizza3.`)
        assert.equal(pizzUni.getRemainingWork(statusArr2), `The following pizzas are still preparing: pizza2, pizza3.`)
        assert.equal(pizzUni.getRemainingWork(statusArr1), 'All orders are complete!')
    })

    it ('orderType', function() {
        assert.equal(pizzUni.orderType(100, 'Delivery'), 100)
        assert.equal(pizzUni.orderType(100, 'Carry Out'), 90)
    })
})
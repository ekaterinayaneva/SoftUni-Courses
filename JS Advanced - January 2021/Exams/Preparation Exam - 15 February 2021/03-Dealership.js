const {assert, expect} = require("chai")
const { describe } = require("mocha")


let dealership = {
    newCarCost: function (oldCarModel, newCarPrice) {

        let discountForOldCar = {
            'Audi A4 B8': 15000,
            'Audi A6 4K': 20000,
            'Audi A8 D5': 25000,
            'Audi TT 8J': 14000,
        }

        if (discountForOldCar.hasOwnProperty(oldCarModel)) {
            let discount = discountForOldCar[oldCarModel];
            let finalPrice = newCarPrice - discount;
            return finalPrice;
        } else {
            return newCarPrice;
        }
    },

    carEquipment: function (extrasArr, indexArr) {
        let selectedExtras = [];
        indexArr.forEach(i => {
            selectedExtras.push(extrasArr[i])
        });

        return selectedExtras;
    },

    euroCategory: function (category) {
        if (category >= 4) {
            let price = this.newCarCost('Audi A4 B8', 30000);
            let total = price - (price * 0.05)
            return `We have added 5% discount to the final price: ${total}.`;
        } else {
            return 'Your euro category is low, so there is no discount from the final price!';
        }
    }
}


describe('dealership', function() {
    describe('newCarCost', function(){
        it('', function() {
            assert.equal(dealership.newCarCost('Audi A4 B8', 30000), 15000)
            assert.equal(dealership.newCarCost('Audi A5', 30000), 30000)
        })
    })
    describe('carEquipment', function(){
        it('', function() {
            assert.deepEqual(dealership.carEquipment(['heated seats', 'sliding roof', 'sport rims', 'navigation'], [0, 2, 3]), ['heated seats', 'sport rims', 'navigation'])
            assert.notDeepEqual(dealership.carEquipment(['ABS', 'sliding roof', 'sport rims', 'navigation'], [0, 2, 3]), ['heated seats', 'sport rims', 'navigation'])
        })
    })
    describe('euroCategory', function(){
        it('', function() {
            assert.equal(dealership.euroCategory(1), 'Your euro category is low, so there is no discount from the final price!')
            assert.equal(dealership.euroCategory(4), `We have added 5% discount to the final price: ${14250}.`)
        })
    })
})

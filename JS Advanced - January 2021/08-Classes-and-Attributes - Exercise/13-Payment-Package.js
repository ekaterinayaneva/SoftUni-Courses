const { assert, expect } = require("chai")

class PaymentPackage {
    constructor(name, value) {
        this.name = name;
        this.value = value;
        this.VAT = 20;      // Default value    
        this.active = true; // Default value
    }

    get name() {
        return this._name;
    }

    set name(newValue) {
        if (typeof newValue !== 'string') {
            throw new Error('Name must be a non-empty string');
        }
        if (newValue.length === 0) {
            throw new Error('Name must be a non-empty string');
        }
        this._name = newValue;
    }

    get value() {
        return this._value;
    }

    set value(newValue) {
        if (typeof newValue !== 'number') {
            throw new Error('Value must be a non-negative number');
        }
        if (newValue < 0) {
            throw new Error('Value must be a non-negative number');
        }
        this._value = newValue;
    }

    get VAT() {
        return this._VAT;
    }

    set VAT(newValue) {
        if (typeof newValue !== 'number') {
            throw new Error('VAT must be a non-negative number');
        }
        if (newValue < 0) {
            throw new Error('VAT must be a non-negative number');
        }
        this._VAT = newValue;
    }

    get active() {
        return this._active;
    }

    set active(newValue) {
        if (typeof newValue !== 'boolean') {
            throw new Error('Active status must be a boolean');
        }
        this._active = newValue;
    }

    toString() {
        const output = [
            `Package: ${this.name}` + (this.active === false ? ' (inactive)' : ''),
            `- Value (excl. VAT): ${this.value}`,
            `- Value (VAT ${this.VAT}%): ${this.value * (1 + this.VAT / 100)}`
        ];
        return output.join('\n');
    }
}


describe('', () => {
    it('constructor', () => {
        let instance = new PaymentPackage('Name', 100)
        assert.equal(instance._name, 'Name')
        assert.equal(instance._value, 100)
        assert.equal(instance._VAT, 20)
        assert.equal(instance._active, true)
    })

    it('name', () => {
        let instance = new PaymentPackage('Name', 100)
        assert.equal(instance.name, 'Name')

        instance.name = 'Merry'

        assert.equal(instance.name, 'Merry')
        assert.throw(() => { instance.name = '' }, 'Name must be a non-empty string')
        assert.throw(() => { instance.name = 1 }, 'Name must be a non-empty string')
    })

    it('value', () => {
        let instance = new PaymentPackage('Name', 100)
        assert.equal(instance.value, 100)

        instance.value = 200

        assert.equal(instance.value, 200)
        assert.throw(() => { instance.value = '' }, 'Value must be a non-negative number', '1')
        assert.throw(() => { instance.value = -1 }, 'Value must be a non-negative number', '2')
        assert.doesNotThrow(() => { instance.value = 0 })
    })

    it('VAT', () => {
        let instance = new PaymentPackage('Name', 100)
        assert.equal(instance.VAT, 20)

        instance.VAT = 50

        assert.equal(instance.VAT, 50)
        assert.throw(() => { instance.VAT = '' }, 'VAT must be a non-negative number')
        assert.throw(() => { instance.VAT = -1 }, 'VAT must be a non-negative number')
    })

    it('active', () => {
        let instance = new PaymentPackage('Name', 100)
        assert.equal(instance.active, true)

        instance.active = false

        assert.equal(instance.active, false)
        assert.throw(() => { instance.active = '' }, 'Active status must be a boolean')
        assert.throw(() => { instance.active = -1 }, 'Active status must be a boolean')
    })

    it('toString', () => {
        function getString(name, value, VAT = 20, active = true) {
            return [
                `Package: ${name}` + (active === false ? ' (inactive)' : ''),
                `- Value (excl. VAT): ${value}`,
                `- Value (VAT ${VAT}%): ${value * (1 + VAT / 100)}`
            ].join('\n')
        }

        let instance = new PaymentPackage('Name', 100)
        assert.equal(instance.toString(), getString('Name', 100))

        instance.VAT = 150
        assert.equal(instance.toString(), getString('Name', 100, 150))

        instance.active = false
        assert.equal(instance.toString(), getString('Name', 100, 150, false))

        instance.name = 'May'
        assert.equal(instance.toString(), getString('May', 100, 150, false))

        instance.value = 3
        assert.equal(instance.toString(), getString('May', 3, 150, false))
    })

})
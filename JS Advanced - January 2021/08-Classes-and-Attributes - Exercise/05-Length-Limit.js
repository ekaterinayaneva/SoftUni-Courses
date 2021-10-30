class Stringer {
    constructor(innerString, innerLength) {
        this.innerString = innerString
        this.innerLength = Number(innerLength)
    }

    increase(length) {
        this.innerLength += length
    }

    decrease(length) {
        this.innerLength -= length
        if (this.innerLength < 0) {
            this.innerLength = 0
        }
    }

    toString() {
        // return this.innerLength >= this.innerString.length ? this.innerString : this.innerString.slice(0, this.innerLength) + '...'
       
        if (this.innerLength == 0) {
            return '...'
        }
        if (this.innerString.length > this.innerLength) {
            return this.innerString.slice(0, this.innerLength) + '...'
        }
        return this.innerString
    }
}


let test = new Stringer("Test", 5);
console.log(test.toString()); // Test

test.decrease(3);
console.log(test.toString()); // Te...

test.decrease(5);
console.log(test.toString()); // ...

test.increase(4); 
console.log(test.toString()); // Test
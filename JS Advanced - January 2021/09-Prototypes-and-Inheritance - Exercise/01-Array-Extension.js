(function solve() {
    Array.prototype.last = function () {
        return this[this.length - 1]
    }

    Array.prototype.skip = function(n) {
        let result = []
        for (let i = n; i < this.length; i++) {
            result.push(this[i])
        }
        return result
    }

    Array.prototype.take = function(n) {
        let result = []
        for (let i = 0; i < n; i++) {
            result.push(this[i])
        }
        return result
    }

    Array.prototype.sum = function() {
        let sum = 0
        for (let i = 0; i < this.length; i++) {
            sum += this[i]
        }
        return sum
    }

    Array.prototype.average = function() {
        return this.sum() / this.length
    }
})()


// ANOTHER SOLUTION
// (() => {
//     Array.prototype.last = function() {
//         return this[this.length-1];
//     };
//     Array.prototype.skip = function(n) {
//         return this.slice(n);
//     };
//     Array.prototype.take = function(n) {
//         return this.slice(0, n);
//     };
//     Array.prototype.sum = function() {
//         return this.reduce((a, x) => a + x, 0);
//     };
//     Array.prototype.average = function() {
//         return this.sum() / this.length;
//     }
// })()

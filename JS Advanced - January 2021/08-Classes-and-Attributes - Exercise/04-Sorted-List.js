class List {
    constructor() {
        this.list = []
        this.size = 0
    }
    
    add(element) {
        this.list.push(element)
        this.list.sort((a,b) => a - b)
        this.size = this.list.length

    }
    
    remove(index) {
        if ((index > this.list.length || index < 0) == false) {
            this.list.splice(index, 1)
            this.size = this.list.length
        }
    }

    get(index) {
        if ((index > this.list.length || index < 0) == false) {
            return this.list[index]
        }
    }
}



let list = new List();
list.add(7);
list.add(6);
list.add(5);
console.log(list.get(1)); 
list.remove(1);
console.log(list.get(1));
console.log(list.size);


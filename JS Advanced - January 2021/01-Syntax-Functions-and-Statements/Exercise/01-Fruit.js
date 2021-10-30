function fruit(fruit, weight, price) {
    const weightKg = weight / 1000
    const money = weightKg * price

    console.log(`I need $${money.toFixed(2)} to buy ${weightKg.toFixed(2)} kilograms ${fruit}.`)
}


fruit('orange', 2500, 1.80)
fruit('apple', 1563, 2.35)

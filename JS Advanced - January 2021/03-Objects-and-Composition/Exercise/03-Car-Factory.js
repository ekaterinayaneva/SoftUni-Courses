function carFactory(carOrder) {

    function getEngine(power) {
        const engines = [
            { power: 90, volume: 1800 },
            { power: 120, volume: 2400 },
            { power: 200, volume: 3500 },
        ]
        return engines.find(engine => engine.power >= power)
    }

    function getCarriage(carriage, color) {
        return {
            type: carriage, color: color
        }
    }

    function getWheels(wheelsize) {
        let wheel = Math.floor(wheelsize) % 2 != 0 ? wheelsize : wheelsize - 1
        return [wheel, wheel, wheel, wheel]             // Array(4).fill(wheel, 0, 4)        moje i bez 0, 4
    }


    return {
        model: carOrder.model,
        engine: getEngine(carOrder.power),
        carriage: getCarriage(carOrder.carriage, carOrder.color),
        wheels: getWheels(carOrder.wheelsize)
    }
}


console.log(carFactory({
    model: 'VW Golf II',
    power: 90,
    color: 'blue',
    carriage: 'hatchback',
    wheelsize: 14
}
))

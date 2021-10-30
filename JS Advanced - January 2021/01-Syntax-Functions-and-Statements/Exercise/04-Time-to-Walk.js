function time(steps, footprintM, speedKM) {
    const speed = speedKM * 1000 / 3600
    const distance = steps * footprintM

    const rest = Math.floor(distance/500) * 60
    const time = distance / speed + rest

    const hours = Math.floor(time / 60 / 60).toFixed(0).padStart(2, '0')
    const minutes = Math.floor((time - hours*3600) / 60).toFixed(0).padStart(2, '0')               // ili samo   time/60
    const seconds = (time - (hours * 60 * 60) - (minutes * 60)).toFixed(0).padStart(2, '0')        // ili samo   time%60

    console.log(`${hours}:${minutes}:${seconds}`)

}


time(4000, 0.60, 5)
time(2564, 0.70, 5.5)
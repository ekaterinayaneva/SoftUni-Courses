function attachEventsListeners() {
    let daysButton = document.getElementById('daysBtn')
    let hoursButton = document.getElementById('hoursBtn')
    let minutesButton = document.getElementById('minutesBtn')
    let secondsButton = document.getElementById('secondsBtn')

    let daysInput = document.getElementById('days')
    let hoursInput = document.getElementById('hours')
    let minutesInput = document.getElementById('minutes')
    let secondsInput = document.getElementById('seconds')

    daysButton.addEventListener('click', () => {
        let days = Number(daysInput.value)
        hoursInput.value = days * 24
        minutesInput.value = days * 24 * 60
        secondsInput.value = days * 24 * 60 * 60
    })

    hoursButton.addEventListener('click', () => {
        let hours = hoursInput.value
        daysInput.value = hours / 24
        minutesInput.value = hours * 60
        secondsInput.value = hours * 60 * 60
    })

    minutesButton.addEventListener('click', () => {
        let minutes = minutesInput.value
        daysInput.value = (minutes / 60) / 24
        hoursInput.value = minutes / 60
        secondsInput.value = minutes * 60
    })

    secondsButton.addEventListener('click', () => {
        let seconds = secondsInput.value
        minutesInput.value = seconds / 60
        hoursInput.value = (seconds / 60) / 60
        daysInput.value = ((seconds / 60) / 60) / 24
    })
}

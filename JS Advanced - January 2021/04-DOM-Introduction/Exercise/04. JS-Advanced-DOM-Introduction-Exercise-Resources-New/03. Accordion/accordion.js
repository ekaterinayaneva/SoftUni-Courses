function toggle() {
    const button = document.getElementsByClassName('button')[0]          // v sluchai che ima poveche ot edin klas 'button' na stranicata
    const text = document.querySelector('#extra')

    console.log(text)

    text.style.display = text.style.display == 'none' || text.style.display == '' ? 'block' : 'none'

    button.textContent = button.textContent == 'More' ? 'Less' : 'More'
}
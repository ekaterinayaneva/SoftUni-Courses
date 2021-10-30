function validate() {
    let input = document.getElementById('email')

    const pattern = /^[a-z]+@[a-z]+.[a-z]+$/gm

    input.addEventListener('change', () => {
        if (pattern.test(input.value) == false) {
            input.classList.add('error')
        } else {
            input.removeAttribute('class')
        }
    })
}
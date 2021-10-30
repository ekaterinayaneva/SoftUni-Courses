function lockedProfile() {
    document.getElementById('main').addEventListener('click', function(ev) {             //ne sabravqi glavniqt element - 'main'
        if (ev.target.tagName === 'BUTTON') {
            const profile = ev.target.parentNode
            const isLocked = profile.querySelector('input[type="radio"]:checked').value == 'lock'
            if (isLocked) {
                return
            }

            let div = profile.querySelector('div')
            let isVisible = div.style.display == 'block'
            div.style.display = isVisible ? 'none' : 'block'

            ev.target.textContent = isVisible ? 'Show more' : 'Hide it'
        }
    })
}
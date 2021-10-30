function addItem() {
    const inputValue = document.getElementById('newItemText')
    const liElement = createElement('li', inputValue.value)                // suzdavem element po funkciq

    const deleteBtn = createElement('a', '[Delete]')
    deleteBtn.href = '#'
    deleteBtn.addEventListener('click', ev => {
        ev.target.parentNode.remove()
    })

    liElement.appendChild(deleteBtn)

    document.getElementById('items').appendChild(liElement)
    inputValue.value = ''

    function createElement(type, content) {                    // suzdaveme funkciq, zashtoto shte suzdavame mn puti 'li' elementi
        const element = document.createElement(type)
        element.textContent = content
        return element
    }
}
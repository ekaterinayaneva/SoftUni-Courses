function addItem() {
    const liElement = document.createElement('li')

    liElement.textContent = document.getElementById('newItemText').value

    const ulElements = document.getElementById('items')

    ulElements.appendChild(liElement)

    document.getElementById('newItemText').value = ''    // izchistvame poleto kudeto pishem
}
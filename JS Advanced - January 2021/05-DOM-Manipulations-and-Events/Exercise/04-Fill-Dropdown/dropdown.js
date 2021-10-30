function addItem() {
    let menu = document.getElementById('menu')
    let inputText = document.getElementById('newItemText')
    let inputValue = document.getElementById('newItemValue')

    let newOption = document.createElement('option')
    newOption.value = inputValue.value
    newOption.textContent = inputText.value
    menu.appendChild(newOption)

    inputText.value = ''
    inputValue.value = ''
}
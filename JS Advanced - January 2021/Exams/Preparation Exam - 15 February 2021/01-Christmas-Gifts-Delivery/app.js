function solution() {
    const input = document.querySelector('input')
    const [gifts, send, discarded] = document.querySelectorAll('section ul')

    document.querySelector('button').addEventListener('click', addGift)

    function addGift() {
        let name = input.value
        input.value = ''

        const element = createEl('li', name, 'gift')
        gifts.appendChild(element) 
        sortGifts()

        const sendBtn = createEl('button', 'Send', 'sendButton')
        const discardBtn = createEl('button', 'Discard', 'discardButton')
        element.appendChild(sendBtn)
        element.appendChild(discardBtn)

        sendBtn.addEventListener('click', () => sendGifts(name, element ))
        discardBtn.addEventListener('click', () => discardGifts(name, element ))
    }

    function sendGifts(name, gift) {
        gift.remove()
        const element = createEl('li', name, 'gift')
        send.appendChild(element)
    }


    function discardGifts(name, gift) {
        gift.remove()
        const element = createEl('li', name, 'gift')
        discarded.appendChild(element)
    }


    function sortGifts() {
        Array
            .from(gifts.children)
            .sort((a, b) => a.childNodes[0].textContent.localeCompare(b.childNodes[0].textContent))
            .forEach(g => gifts.appendChild(g));
    }


    function createEl(type, content, className) {
        const result = document.createElement(type);
        result.textContent = content;
        if (className) {
            result.className = className;
        }
        return result;
    }
}
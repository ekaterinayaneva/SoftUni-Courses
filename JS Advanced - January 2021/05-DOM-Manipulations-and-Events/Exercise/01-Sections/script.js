function create(words) {
   const content = document.getElementById('content')

   for (const word of words) {
      const div = document.createElement('div')
      const paragraph = document.createElement('p')
      paragraph.textContent = word
      paragraph.style.display = 'none'
      div.appendChild(paragraph)
      div.addEventListener('click', function(ev) {
         const p = ev.target.children[0]
         const isVisible = p.style.display == 'block'
         p.style.display = isVisible ? 'none' : 'block'
      })

      content.appendChild(div)
   }
}
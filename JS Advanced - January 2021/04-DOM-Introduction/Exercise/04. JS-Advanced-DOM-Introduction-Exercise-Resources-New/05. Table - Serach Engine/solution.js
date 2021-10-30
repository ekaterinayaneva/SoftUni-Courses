function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      const rows = document.querySelectorAll('tbody tr')
      const input = document.getElementById('searchField').value   //querySelector('#searchField').value

      for (const row of rows) {
         if ((row.textContent).toLowerCase().includes(input.toLowerCase())) {
            row.setAttribute('class', 'select')
         }else {
            row.removeAttribute('class')
         }
      }
   }
}
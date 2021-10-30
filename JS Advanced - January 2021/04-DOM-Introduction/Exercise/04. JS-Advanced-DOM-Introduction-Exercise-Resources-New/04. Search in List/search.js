function search() {
   const towns = document.querySelectorAll('#towns>li')
   let input = document.getElementById('searchText').value
   let result = document.getElementById('result')

   sum = 0

   for (const town of towns) {
      if ((town.textContent).toLowerCase().includes(input.toLocaleLowerCase()) && input != '') {
         town.style.fontWeight = 'bold'
         town.style.textDecoration = 'underline'
         sum ++
      }else{
         town.style.fontWeight = ''
         town.style.textDecoration = ''
      }
   }
   result.textContent = `${sum} matches found`
}

// function deleteByEmail() {
//     const email = document.querySelector('input[name="email"]').value

//     const rows = Array.from(document.querySelectorAll('tbody tr'))         // Array.from zaradi judge

//     let deleted = false

//     for (const row of rows) {
//         if (row.children[1].textContent == email) {
//             row.remove()                                 //  row.parentNode.removeChild(row)
//             deleted = true
//             document.getElementById('result').textContent = 'Deleted.'
//         }
//     }
//     if (deleted == false) {
//         document.getElementById('result').textContent = 'Not found.'

//     }
// }


function deleteByEmail() {
    const email = document.querySelector('input[name="email"]').value
    const resultElement = document.getElementById('result')

    const rows = Array.from(document.querySelectorAll('tbody tr'))         // Array.from zaradi judge

    const matches = rows.filter(r => r.children[1].textContent == email)
    
    if (matches.length > 0) {
        matches.forEach(r => r.remove())
        resultElement.textContent = 'Deleted.'
    }else{
        resultElement.textContent = 'Not found.'
    }
}
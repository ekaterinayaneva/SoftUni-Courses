function solve() {
    let input = document.getElementById('text').value;
    let currentCase = document.getElementById('naming-convention').value;
    let output = document.getElementById('result');
  
    input = input.toLowerCase();
  
    let outputArr = [];
  
    if(currentCase == 'Camel Case'){
      input = input.split(' ');
      outputArr = input.splice(0, 1);
      while(input.length > 0){
        let word = input.shift();
        word = word.charAt(0).toUpperCase() + word.slice(1);
        outputArr.push(word);
      }
      output.textContent = `${outputArr.join('')}`;
    } else if(currentCase == 'Pascal Case'){
      input = input.split(' ');
      while(input.length > 0){
        let word = input.shift();
        word = word.charAt(0).toUpperCase()+word.slice(1);
        outputArr.push(word);
      }
      output.textContent = `${outputArr.join('')}`;
    } else {
      output.textContent = 'Error!'
    }
  }
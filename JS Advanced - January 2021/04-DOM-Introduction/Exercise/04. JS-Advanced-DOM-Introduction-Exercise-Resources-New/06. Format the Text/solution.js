function solve() {
  let textArea = document.getElementById('input');
  let button = document.getElementById('formatItBtn');
  let sentences = textArea.value.split('.')
    .filter(x => x.length > 0);
  textArea.value = '';
  let paragraphs = Math.ceil(sentences.length / 3);
  let ouput = document.getElementById('output');
  for (let i = 0; i < paragraphs; i++) {
    let pElement = document.createElement('p');
    let res = [];
    for (let j = 0; j < 3; j++) {
      if (sentences.length === 0) {
        break;
      }

      res.push(sentences.shift());
    }

    let result = res.join('.');
    if (!result.endsWith('.')) {
      result += '.';
    }
    pElement.textContent = result;
    ouput.appendChild(pElement);
  }
}
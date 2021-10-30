function solve() {
  const inputs = document.querySelectorAll('textarea');
  const buttons = document.querySelectorAll('button');
  const tbody = document.querySelector('tbody');

  buttons[0].addEventListener('click', function (ev) {
    const pieces = JSON.parse(inputs[0].value);

    for (const piece of pieces) {
      const row = document.createElement('tr')

      const nameCell = createFurniturePiece('p', piece.name);
      const imageCell = createFurniturePiece('img', '', ['src', piece.img]);
      const priceCell = createFurniturePiece('p', Number(piece.price));
      const decorFactorCell = createFurniturePiece('p', Number(piece.decFactor));
      const btnCell = createFurniturePiece('input', '', ['type', 'checkbox']);

      row.appendChild(imageCell);
      row.appendChild(nameCell);
      row.appendChild(priceCell);
      row.appendChild(decorFactorCell);
      row.appendChild(btnCell);

      tbody.appendChild(row)
    }
  });

  buttons[1].addEventListener('click', function (ev) {
    const checkboxes = document.querySelectorAll('tr td input');

    const output = {
      names: [],
      price: 0,
      decFac: 0
    }

    for (const checkbox of checkboxes) {
      if (checkbox.checked) {
        const tr = checkbox.parentElement.parentElement;
        const name = tr.children[1].children[0].textContent;
        const price = Number(tr.children[2].children[0].textContent);
        const deFac = Number(tr.children[3].children[0].textContent);

        output.names.push(name);
        output.price += price;
        output.decFac += deFac;
      }
    }

    inputs[1].value = `Bought furniture: ${output.names.join(', ')}\nTotal price: ${output.price.toFixed(2)}\nAverage decoration factor: ${output.decFac / output.names.length}`
  })

  function createFurniturePiece(type, text, attribute) {
    const cell = document.createElement('td');
    const elem = document.createElement(type);
    if (attribute) {
      elem.setAttribute(attribute[0], attribute[1])
    }
    elem.textContent = text;
    cell.appendChild(elem);

    return cell;
  }
}

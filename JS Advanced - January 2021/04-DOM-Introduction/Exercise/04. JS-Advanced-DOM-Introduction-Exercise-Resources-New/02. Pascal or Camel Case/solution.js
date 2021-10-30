function solve() {
  const text = document.getElementById('text').textContent
  const namingConvention = document.getElementById('naming-convention').textContent
  const result = document.getElementById('result')

  const modifiedStr = ''

  if (namingConvention == 'Pascal Case') {
    modifiedStr = text =>
      text
        .toLowerCase()
        .replace(/\w\S*/g, m => m.chartAt(0).toUpperCase + m.substr(1).toLowerCase())
  }
  else if (namingConvention == 'Camal Case') {
    modifiedStr = text =>
      text
        .toLowerCase()
        .replace(/[^a-zA-Z0-9]+(.)/g, (m, chr) => chr.toUpperCase())
  }
  result.textContent = `${modifiedStr}`
}
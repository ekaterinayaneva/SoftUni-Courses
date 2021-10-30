function editElement(ref, match, replacer) {
    const matcher = newRegExp(match, 'g')
    const result = ref.textContent.replace(matcher, replacer)
    ref.textContent = result
}


editElement(a1, '%insert name here%', 'Document Object Model')


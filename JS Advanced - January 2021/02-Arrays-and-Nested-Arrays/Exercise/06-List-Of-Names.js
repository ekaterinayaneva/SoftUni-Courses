function solve(arr) {
    let result = arr
        .slice(0)                                  // pravim si nov masiv, koeto v sluchaq ne ni trqbva
        .sort((a, b) => a.localeCompare(b))
        .map((name, index) => {
            let result = `${index + 1}.${name} `
            return result
        })

    return result.join('\n')
}


console.log(solve(["John", "Bob", "Christina", "Ema"]))
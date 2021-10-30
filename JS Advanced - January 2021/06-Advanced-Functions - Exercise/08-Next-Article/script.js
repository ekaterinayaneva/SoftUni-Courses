function getArticleGenerator(articles) {
    const content = document.getElementById('content')

    return next = () => {
        let info = articles.shift()

        if (info != undefined) {
            let article = document.createElement('article')
            article.textContent = info
            content.appendChild(article)
            return content
        }
  
    }
}

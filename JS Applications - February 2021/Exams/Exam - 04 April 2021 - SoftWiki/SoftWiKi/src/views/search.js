import { html } from '../../node_modules/lit-html/lit-html.js'
import { searchArticle } from '../api/data.js';

const searchTemplate = (data, onSubmit) => html`
<section id="search-page" class="content">
    <h1>Search</h1>
    <form @submit=${onSubmit} id="search-form">
        <p class="field search">
            <input id = 'searchField' type="text" placeholder="Search by article title" name="search">
        </p>
        <p class="field submit">
            <input id = 'searchBtn' class="btn submit" type="submit" value="Search">
        </p>
    </form>
    <div class="search-container">

        ${data.length > 0 ? html`${data.map(itemTemplate)}` : html`<h3 class="no-articles">
        No matching articles
        </h3>`}

    </div>
</section>`;

const itemTemplate = (item) => html`
 <a class="article-preview" href="/details/${item._id}">
        <article>
            <h3>Topic: <span>${item.title}</span></h3>
            <p>Category: <span>${item.category}</span></p>
        </article>
    </a>`;


export async function searchPage(ctx) {
    let data = []
    ctx.render(searchTemplate(data, onSubmit));
    
    async function onSubmit(ev) {
        ev.preventDefault();
        const formData = new FormData(ev.target);

        const query = formData.get('search');

        data = await searchArticle(query);
    
        ctx.render(searchTemplate(data, onSubmit))
    }

}
import { html } from '../../node_modules/lit-html/lit-html.js';
import { getCatalog } from '../api/data.js';


const catalogTemplate = (items) => html`
<section id="catalog-page" class="content catalogue">
    <h1>All Articles</h1>

    ${items.length == 0 ? html`<h3 class="no-articles">
    No articles yet
    </h3>` : items.map(itemTemplate)}

</section>`

const itemTemplate = (item) => html`
<a class="article-preview" href="/details/${item._id}">
    <article>
        <h3>Topic: <span>${item.title}</span></h3>
        <p>Category: <span>${item.category}</span></p>
    </article>
</a>`


export async function catalogPage(ctx) {
    const items = await getCatalog();

    ctx.render(catalogTemplate(items));           
    ctx.setUserNav();
}

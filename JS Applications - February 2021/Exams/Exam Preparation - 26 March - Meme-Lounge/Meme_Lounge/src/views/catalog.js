import { html } from '../../node_modules/lit-html/lit-html.js';
import { getCatalog } from '../api/data.js';


const catalogTemplate = (items) => html`
<section id="meme-feed">
    <h1>All Memes</h1>
    <div id="memes">
        

    ${items.length == 0 ? html`<p class="no-memes">
        No memes in database.
    </p>` : items.map(itemTemplate)}


    </div>
</section>`


const itemTemplate = (item) => html`
<div class="meme">
    <div class="card">
        <div class="info">
            <p class="meme-title">${item.title}</p>
            <img class="meme-image" alt="meme-img" src="${item.imageUrl}">
        </div>
        <div id="data-buttons">
            <a class="button" href="/details/${item._id}">Details</a>
        </div>
    </div>
</div>`

export async function catalogPage(ctx) {
    const items = await getCatalog();

    ctx.render(catalogTemplate(items));
    ctx.setUserNav();
}
import { html } from '../../node_modules/lit-html/lit-html.js';
import { getHome } from '../api/data.js';

const homeTemplate = (items) => html`
<section id="home-page" class="content">
    <h1>Recent Articles</h1>
    
    <section class="recent js"> 
    <h2>JavaScript</h2>
        ${(items.filter(x => x.category === 'JavaScript').length !== 0)
        ? items.filter(x => x.category === 'JavaScript').map(itemTemplate)
        : html`<h3 class="no-articles">No articles yet</h3>`}
    </section>
    
    <section class="recent csharp">
        <h2>C#</h2>
        ${(items.filter(x => x.category === 'C#').length !== 0)
        ? items.filter(x => x.category === 'C#').map(itemTemplate)
        : html`<h3 class="no-articles">No articles yet</h3>`}
    </section>
    
    <section class="recent java">
        <h2>Java</h2>
        ${(items.filter(x => x.category === 'Java').length !== 0)
        ? items.filter(x => x.category === 'Java').map(itemTemplate)
        : html`<h3 class="no-articles">No articles yet</h3>`}
    </section>
    
    <section class="recent python">
        <h2>Python</h2>
        ${(items.filter(x => x.category === 'Python').length !== 0)
        ? items.filter(x => x.category === 'Python').map(itemTemplate)
        : html`<h3 class="no-articles">No articles yet</h3>`}
    </section>
</section>`

const itemTemplate = (item) => html`
<article>
    <h3>${item.title}</h3>
    <p>${item.content}</p>
    <a href="/details/${item._id}" class="btn details-btn">Details</a>
</article>`

export async function homePage(ctx) {
    const items = await getHome();   

    ctx.render(homeTemplate(items));
    ctx.setUserNav()

}

import { html } from '../../node_modules/lit-html/lit-html.js';
import { getDetails, deleteRecord } from '../api/data.js'


const detailsTemplate = (item, isOwner, onDelete) => html`
<section id="details-page" class="content details">
    <h1>${item.title}</h1>

    <div class="details-content">
        <strong>Published in category ${item.category}</strong>
        <p>${item.content}</p>

        
        <div class="buttons">
        ${isOwner ? html`
            <a @click=${onDelete} class="btn delete">Delete</a>
            <a href="/edit/${item._id}" class="btn edit">Edit</a>` : ''} 
            <a href="/home" class="btn edit">Back</a>
        </div>
    </div>
</section>`



export async function detailsPage(ctx) {
    const id = ctx.params.id;
    const item = await getDetails(id);
    const userId = sessionStorage.getItem('userId')

    const isOwner = userId === item._ownerId

    ctx.render(detailsTemplate(item, isOwner, onDelete));   

    async function onDelete() {
        const confirmed = confirm('Are you sure you want to delete this item?');
        if (confirmed) {
            await deleteRecord(id)
            ctx.page.redirect('/');
        }
    }
}

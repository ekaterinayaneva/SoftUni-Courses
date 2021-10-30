import { html } from '../../node_modules/lit-html/lit-html.js';
import { editRecord, getDetails } from '../api/data.js'

const editTemplate = (item, onSubmit) => html`
<section id="edit-page" class="content">
    <h1>Edit Article</h1>

    <form  @submit=${onSubmit} id="edit">
        <fieldset>
            <p class="field title">
                <label for="title">Title:</label>
                <input type="text" name="title" id="title" placeholder="Enter article title" .value=${item.title}>
            </p>

            <p class="field category">
                <label for="category">Category:</label>
                <input type="text" name="category" id="category" placeholder="Enter article category" .value=${item.category}>
            </p>
            <p class="field">
                <label for="content">Content:</label>
                <textarea name="content" id="content" .value=${item.content}></textarea>
            </p>

            <p class="field submit">
                <input class="btn submit" type="submit" value="Save Changes">
            </p>

        </fieldset>
    </form>
</section>`


export async function editPage(ctx) {
    const id = ctx.params.id;
    const item = await getDetails(id);

    ctx.render(editTemplate(item, onSubmit));

    async function onSubmit(event) {
        event.preventDefault();
        const formData = new FormData(event.target);

        const data = {
            title: formData.get('title'),
            category: formData.get('category'),
            content: formData.get('content'),
        }


        if (Object.values(data).some(x => !x)) {
            return alert('All fields are required!');
        }

        await editRecord(item._id, data);

        event.target.reset();

        ctx.page.redirect('/details/' + id);
    }
}
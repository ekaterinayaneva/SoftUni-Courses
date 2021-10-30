import { html } from '../../node_modules/lit-html/lit-html.js';
import { createRecord } from '../api/data.js'

const createTemplate = (onSubmit) => html`
<section id="create-page" class="content">
    <h1>Create Article</h1>

    <form @submit=${onSubmit} id="create">
        <fieldset>
            <p class="field title">
                <label for="create-title">Title:</label>
                <input type="text" id="create-title" name="title" placeholder="Enter article title">
            </p>

            <p class="field category">
                <label for="create-category">Category:</label>
                <input type="text" id="create-category" name="category" placeholder="Enter article category">
            </p>
            <p class="field">
                <label for="create-content">Content:</label>
                <textarea name="content" id="create-content"></textarea>
            </p>

            <p class="field submit">
                <input class="btn submit" type="submit" value="Create">
            </p>

        </fieldset>
    </form>
</section>`

export async function createPage(ctx) {
    ctx.render(createTemplate(onSubmit));

    async function onSubmit(event) {
        event.preventDefault();
        const formData = new FormData(event.target);

        let title = formData.get('title');
        let category = formData.get('category');
        let content = formData.get('content');
        
        if(title === ''||category ===''|| content === ''){
           return window.alert('all fields must be filled');
        }

        let categoryContent = ['JavaScript', 'C#', 'Java', 'Python'];
        if(categoryContent.includes(category) == false){
           return window.alert('Category not correct');
        }

        const data = {
            title,
            category,
            content
        };

        await createArticle(data);

     //   ctx.setUserNav();
        ctx.page.redirect('/');
    }
}

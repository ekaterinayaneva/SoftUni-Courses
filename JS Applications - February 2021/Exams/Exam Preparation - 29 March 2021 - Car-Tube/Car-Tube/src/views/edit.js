import { html } from '../../node_modules/lit-html/lit-html.js';
import { editRecord, getDetails } from '../api/data.js'

const editTemplate = (item, onSubmit) => html`
<section id="edit-listing">
    <div class="container">

        <form @submit=${onSubmit} id="edit-form">
            <h1>Edit Car Listing</h1>
            <p>Please fill in this form to edit an listing.</p>
            <hr>

            <p>Car Brand</p>
            <input type="text" placeholder="Enter Car Brand" name="brand" .value=${item.brand}>

            <p>Car Model</p>
            <input type="text" placeholder="Enter Car Model" name="model" .value=${item.model}>

            <p>Description</p>
            <input type="text" placeholder="Enter Description" name="description" .value=${item.description}>

            <p>Car Year</p>
            <input type="number" placeholder="Enter Car Year" name="year" .value=${item.year}>

            <p>Car Image</p>
            <input type="text" placeholder="Enter Car Image" name="imageUrl" .value=${item.imageUrl}>

            <p>Car Price</p>
            <input type="number" placeholder="Enter Car Price" name="price" .value=${item.price}>

            <hr>
            <input type="submit" class="registerbtn" value="Edit Listing">
        </form>
    </div>
</section>`


export async function editPage(ctx) {
    const id = ctx.params.id;
    const item = await getDetails(id);

    ctx.render(editTemplate(item, onSubmit));

    async function onSubmit(event) {
        event.preventDefault();
        const formData = new FormData(event.target);

        // const title = formData.get('title').trim();
        // const description = formData.get('description').trim();
        // const imageUrl = formData.get('imageUrl').trim();

        const data = {
            brand: formData.get('brand'),
            model: formData.get('model'),
            description: formData.get('description'),
            year: Number(formData.get('year')),
            imageUrl: formData.get('imageUrl'),
            price: Number(formData.get('price')),
        }


        if (data.year < 0 || data.price < 0) {
            return alert('Year and Price must be positive number!')
        }

        if (Object.values(data).some(x => !x)) {
            return alert('All fields are required!');
        }

        await editRecord(item._id, data);

        event.target.reset();

        ctx.page.redirect('/details/' + id);
    }
}
import { html } from '../../node_modules/lit-html/lit-html.js';
import { getCatalog } from '../api/data.js';


const catalogTemplate = (pets) => html`
<!-- Dashboard Page ( for Guests and Users ) -->
<section id="dashboard-page" class="dashboard">
    <h1>Dashboard</h1>

    ${pets.length == 0 ? html`<p class="no-pets">
    No pets in database!
    </p>` : pets.map(itemTemplate)}

</section>`


const itemTemplate = (pet) => html`
<ul class="other-pets-list">

    <li class="otherPet">
        <h3>Name: ${pet.name}</h3>
        <p>Type: ${pet.type}</p>
        <p class="img"><img src="${pet.imageUrl}"></p>
        <a class="button" href="details/${pet._id}">Details</a>
    </li>

</ul>`

export async function catalogPage(ctx) {
    const pets = await getCatalog();

    ctx.render(catalogTemplate(pets));
    ctx.setUserNav();
}
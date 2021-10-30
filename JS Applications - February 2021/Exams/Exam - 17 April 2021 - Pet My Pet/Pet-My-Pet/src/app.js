import { render } from '../node_modules/lit-html/lit-html.js';
import page from '../node_modules/page/page.mjs';


import { loginPage } from './views/login.js';
import { registerPage } from './views/register.js';
import { logout } from './api/api.js';
import { catalogPage } from './views/catalog.js';
import { createPage } from './views/create.js';
import { detailsPage} from './views/details.js';
import { editPage} from './views/edit.js';
import { myProfilePage} from './views/profile.js';

const main = document.getElementById('site-content');


setUserNav();

page('/login', decorateContext, loginPage);
page('/register', decorateContext, registerPage);
page('/catalog', decorateContext, catalogPage);
page('/create', decorateContext, createPage);
page('/details/:id', decorateContext, detailsPage);
page('/edit/:id', decorateContext, editPage);
page('/profile', decorateContext, myProfilePage);

page.start();


function decorateContext(ctx, next) {
    ctx.render = (content) => render(content, main);
    ctx.setUserNav = setUserNav;
    next();
}

function setUserNav() {
    const email = sessionStorage.getItem('email');
    if (email) {
        document.querySelector('div#user > span').textContent = `Welcome, ${email}`;
        document.getElementById('user').style.display = 'block';
        document.getElementById('guest').style.display = 'none';
    } else {
        document.getElementById('user').style.display = 'none';
        document.getElementById('guest').style.display = 'block';
    }
}


document.getElementById('logoutBtn').addEventListener('click', async () => {
    await logout();
    page.redirect('/catalog');
    setUserNav();    
})
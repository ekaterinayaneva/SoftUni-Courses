import { render } from '../node_modules/lit-html/lit-html.js';
import page from '../node_modules/page/page.mjs';

import { logout } from './api/api.js';
import { logout as apiLogout } from './api/data.js'      //logout
import { homePage } from './views/home.js';
import { loginPage } from './views/login.js';
import { registerPage } from './views/register.js';
import { catalogPage } from './views/catalog.js';
import { createPage } from './views/create.js';
import { detailsPage} from './views/details.js';
import { editPage} from './views/edit.js';
import { myProfilePage} from './views/my-profile.js';

const main = document.querySelector('main');
// document.getElementById('logoutBtn').addEventListener('click', logout);   //logout

setUserNav();

page('/', decorateContext, homePage);
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
    if (email != null) {
        document.querySelector('div.profile > span').textContent = `Welcome, ${email}`;
        document.querySelector('.user').style.display = '';
        document.querySelector('.guest').style.display = 'none';
    } else {
        document.querySelector('.user').style.display = 'none';
        document.querySelector('.guest').style.display = '';
    }
}


//logout
// async function logout() {
//     await apiLogout();
//     setUserNav();
//     page.redirect('/');
// }


document.getElementById('logoutBtn').addEventListener('click', async () => {
    await logout();
    page.redirect('/');
    setUserNav();    
})
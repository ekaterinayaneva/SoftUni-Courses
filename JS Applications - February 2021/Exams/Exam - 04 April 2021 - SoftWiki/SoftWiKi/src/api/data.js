import * as api from './api.js';

const host = 'http://localhost:3030';
api.settings.host = 'http://localhost:3030';

export const login = api.login;
export const register = api.register;
export const logout = api.logout;


export async function getCatalog() {                    // catalog 
    return await api.get(host + '/data/wiki?sortBy=_createdOn%20desc');
}

export async function getHome() {                    // home
    return await api.get(host + '/data/wiki?sortBy=_createdOn%20desc&distinct=category');
}

export async function getDetails(id) {                  // details
    return await api.get(host + '/data/wiki/' + id);
}


export async function createRecord(data) {                // create
    return await api.post(host + '/data/wiki', data);
}

export async function editRecord(id, data) {                // edit
    return await api.put(host + '/data/wiki/' + id, data);
}

export async function deleteRecord(id) {                // delete
    return await api.del(host + '/data/wiki/' + id);
}


export async function searchArticle(query){             // search
    return api.get(host + `/data/wiki?where=title%20LIKE%20%22${query}%22`);
}

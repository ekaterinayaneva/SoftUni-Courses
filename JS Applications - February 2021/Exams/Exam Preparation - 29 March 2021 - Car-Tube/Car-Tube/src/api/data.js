import * as api from './api.js';

const host = 'http://localhost:3030';
api.settings.host = 'http://localhost:3030';

export const login = api.login;
export const register = api.register;
export const logout = api.logout;


export async function getCatalog() {                    // catalog / all items
    return await api.get(host + '/data/cars?sortBy=_createdOn%20desc');
}

export async function getMyItems() {                // my items    
    const userId = sessionStorage.getItem('userId')
    return await api.get(host + `/data/cars?where=_ownerId%3D%22${userId}%22&sortBy=_createdOn%20desc`);
}

export async function getDetails(id) {                  // details
    return await api.get(host + '/data/cars/' + id);
}


export async function createRecord(data) {                // create
    return await api.post(host + '/data/cars/', data);
}

export async function editRecord(id, data) {                // edit
    return await api.put(host + '/data/cars/' + id, data);
}

export async function deleteRecord(id) {                // delete
    return await api.del(host + '/data/cars/' + id);
}

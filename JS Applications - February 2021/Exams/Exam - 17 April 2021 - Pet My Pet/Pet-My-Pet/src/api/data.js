import * as api from './api.js';

const host = 'http://localhost:3030';
api.settings.host = host;

export const login = api.login;
export const register = api.register;
export const logout = api.logout;


export async function getCatalog() {                                      // dashboard
    return await api.get(host + '/data/pets?sortBy=_createdOn%20desc');
}

export async function getMyItems() {                                     // my pets    
    const userId = sessionStorage.getItem('userId')
    return await api.get(host + `/data/pets?where=_ownerId%3D%22${userId}%22&sortBy=_createdOn%20desc`);
}

export async function getDetails(id) {                                  // details
    return await api.get(host + '/data/pets/' + id);
}


export async function createRecord(data) {                              // create
    return await api.post(host + '/data/pets', data);
}

export async function editRecord(id, data) {                           // edit
    return await api.put(host + '/data/pets/' + id, data);
}

export async function deleteRecord(id) {                              // delete
    return await api.del(host + '/data/pets/' + id);
}

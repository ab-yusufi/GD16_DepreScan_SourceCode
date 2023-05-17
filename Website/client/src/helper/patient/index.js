export const getAllPatients = () => {
    return fetch(`/api/patients`, {
        method: 'GET'
    }).then(res => {
        console.log(res)
        return res.json();
    })
    .catch(err => console.log(err));
}
export const getAllCategories = () => {
    return fetch('/api/categories', {
        method: "GET"
    })
    .then(res => res.json())
    .catch(err => console.log(err));
}
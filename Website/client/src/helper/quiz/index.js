export const createQuiz = (userId, token, quiz) => {
    return fetch(`/api/quiz/create/${userId}`, {
        method: 'POST',
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`
        },
        body: JSON.stringify(quiz)
    }).then(res => res.json())
    .catch(err => console.log(err));
}
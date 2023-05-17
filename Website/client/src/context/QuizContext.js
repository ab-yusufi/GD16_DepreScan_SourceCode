import React, { createContext, useState } from 'react';

export const QuizContext = createContext();

export const QuizProvider = ({children}) => {
    const [quiz, setQuiz] = useState({
        q1: ["", "", "", "", "", ""],
        q2: ["", "", "", "", "", ""],
        q3: ["", "", "", "", "", ""],
        q4: ["", "", "", "", "", ""],
        q5: ["", "", "", "", "", ""],
        category: "",
        marks: 5
    })
    return(
        <QuizContext.Provider value={[quiz, setQuiz]}>
          {children}
        </QuizContext.Provider>
    )
}
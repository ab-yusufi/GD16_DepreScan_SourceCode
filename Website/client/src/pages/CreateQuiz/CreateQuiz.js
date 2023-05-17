// import React, { Fragment, useContext, useState, useEffect } from "react";
// import './CreateQuiz.css'
// import { Redirect } from "react-router";
// import PrimaryButton from "../../components/PrimaryButton/PrimaryButton";
// import QuestionCard from "../../components/QuestionCard/QuestionCard";
// import Base from "../Base/Base";
// import { QuizContext, QuizProvider } from "../../context/QuizContext";
// import { createQuiz } from "../../helper/quiz";
// import { isAuthenticated } from "../../helper/auth";
// import { getAllCategories } from "../../helper/category";
// import DropDown from './../../components/DropDown/DropDown';

// const CreateQuiz = () => {

//   const [quiz, setQuiz] = useContext(QuizContext)  
//   const [categories, setCategories] = useState([]);
//   const {user, token} = isAuthenticated();

//   useEffect(() => {
//     getAllCategories()
//       .then(data => {
//         setCategories(data);
//       })
//       .catch(err => console.log(err));
//   }, [])

//   // const handleChange = (name) => (event) => {
//   //   setQuiz({ ...quiz, [name]: event.target.value });
//   // };
  
//   const handleSubmit = () => {
//     createQuiz(user._id, token, quiz)
//       .then(res => console.log(res))
//       .catch(err => console.log(err));
    
//     setQuiz({
//       q1: ["", "", "", "", "", ""],
//       q2: ["", "", "", "", "", ""],
//       q3: ["", "", "", "", "", ""],
//       q4: ["", "", "", "", "", ""],
//       q5: ["", "", "", "", "", ""],
//       category: "",
//       marks: 5
//     });
//   }

//   return (
//     <Base>
//       <Fragment> 
//       <div className="heading">
//         <h1>Welcome, Create Your Quiz Here</h1>
//       </div>
//       <div className="nameInput">
//         <input type="text" placeholder="Enter Your Name"/>
//       </div>
//       <DropDown values={categories}/>
//       <div className="qCardContainer">
//          <QuestionCard number={"q1"}/> 
//          <QuestionCard number={"q2"}/> 
//          <QuestionCard number={"q3"}/> 
//          <QuestionCard number={"q4"}/> 
//          <QuestionCard number={"q5"}/> 
//          <PrimaryButton title="Add" onClick={()=>{}}/>
//       </div>
//       <div>
//         <PrimaryButton title="Done" onClick={handleSubmit}/>
//       </div>
//       </Fragment>
//     </Base>
//   );
// };

// export default CreateQuiz;

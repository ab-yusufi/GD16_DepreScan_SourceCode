const express = require("express");
const router = express.Router();

const { isSignedIn, isAuthenticated, isAdmin } = require("../controllers/auth");
const { getCategoryById } = require("../controllers/category");
const { getQuizById, getAllQuizes, createQuiz, updateQuiz, deleteQuiz, getQuiz } = require("../controllers/quiz");
const { getUserById } = require("../controllers/user");

router.param("userId", getUserById);
router.param("quizId", getQuizById);
router.param("categoryId", getCategoryById);

router.post("/quiz/create/:userId", isSignedIn, isAuthenticated, createQuiz);
router.get("/quizes", getAllQuizes);
router.get("/quiz/:quizId", getQuiz);
router.put("/quiz/:userId/:quizId", isSignedIn, isAuthenticated, updateQuiz);
router.delete("/quiz/:userId/:quizId", isSignedIn, isAuthenticated, deleteQuiz);

module.exports = router;
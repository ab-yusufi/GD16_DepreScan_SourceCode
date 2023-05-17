const express = require('express');
const { getAttemptById, attemptQuiz, getAllAttempts, getAttempt, attemptAuthQuiz } = require('../controllers/attempt');
const { isSignedIn, isAuthenticated } = require('../controllers/auth');
const { getQuizById } = require('../controllers/quiz');
const { getUserById } = require('../controllers/user');
const router = express.Router();


router.param("quizId", getQuizById);
router.param("attemptId", getAttemptById);
router.param("userId", getUserById);

router.post("/quiz/attempt/:quizId/:userId", isSignedIn, isAuthenticated, attemptAuthQuiz);
router.post("/quiz/attempt/:quizId/", attemptQuiz);
router.get("/quiz/attempts/:quizId", getAllAttempts);
router.get("/quiz/attempt/:attemptId/:quizId", getAttempt);

module.exports = router;
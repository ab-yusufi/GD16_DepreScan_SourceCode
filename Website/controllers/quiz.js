const Quiz = require("../models/quiz");

exports.getQuizById = (req, res, next, id) => {
  Quiz.findById(id).exec((err, quiz) => {
    if (err || !quiz) {
      return res.status(400).json({
        error: "No quiz was found in DB",
      });
    }
    req.quiz = quiz;
    next();
  });
};

exports.getAllQuizes = (req, res) => {
  Quiz.find().exec((err, quizes) => {
    if (err) {
      return res.status(400).json({
        error: "NO quizes found",
      });
    }
    res.json(quizes);
  });
};

exports.getQuiz = (req, res) => {
  return res.json(req.quiz);
};

exports.createQuiz = (req, res) => {
  req.body.uid = req.profile;
  // req.body.category = req.category;
  const quiz = new Quiz(req.body);
  quiz.save((err, quiz) => {
    if (err) {
      console.log(err);
      return res.status(400).json({
        error: "Failed to save in your DB",
      });
    }
    res.json(quiz);
  });
};

exports.updateQuiz = (req, res) => {
  Quiz.findByIdAndUpdate(
    { _id: req.quiz._id },
    { $set: req.body },
    { new: true, useFindAndModify: false },
    (err, quiz) => {
      if (err) {
        return res.status(400).json({
          error: "You are not authorized to update this user",
        });
      }
      res.json(quiz);
    }
  );
};

exports.deleteQuiz = (req, res) => {
  const quiz = req.quiz;
  quiz.remove((err, quiz) => {
    if (err) {
      return res.status(400).json({
        error: "Failed to delete this quiz",
      });
    }
    res.json({
      message: "Successfull deleted quiz",
    });
  });
};

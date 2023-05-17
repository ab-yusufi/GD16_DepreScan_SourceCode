const Attempt = require("../models/attempt");

exports.getAttemptById = (req, res, next, id) => {
    Attempt.findById(id).exec((err, attempt) => {
      if (err || !attempt) {
        return res.status(400).json({
          error: "No attempt was found in DB"
        });
      }
      req.attempt = attempt;
      next();
    });
};

exports.getAllAttempts = (req, res) => {
    Attempt.find().exec((err, attempts) => {
      if (err) {
        return res.status(400).json({
          error: "NO attempts found"
        });
      }
      res.json(attempts);
    });
  };

exports.getAttempt = (req, res) => {
  return res.json(req.attempt)
}

exports.attemptQuiz = (req, res) => {
    req.body.quiz = req.quiz
    req.body.outof = req.quiz.marks
    const attempt = new Attempt(req.body)
    attempt.save((err, attempt) => {
        if(err){
            console.log(err)
            return res.status(400).json({
                error: "Failed to save in your DB"
            });
        }
        res.json(attempt);
    })
}


exports.attemptAuthQuiz = (req, res) => {
    req.body.quiz = req.quiz
    req.body.outof = req.quiz.marks
    req.body.uid = req.profile
    req.body.name = req.profile.username
    const attempt = new Attempt(req.body)
    attempt.save((err, attempt) => {
        if(err){
            console.log(err)
            return res.status(400).json({
                error: "Failed to save in your DB"
            });
        }
        res.json(attempt);
    })
}
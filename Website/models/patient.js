const mongoose = require("mongoose");

var patientSchema = new mongoose.Schema({
    patientName: String,
    patientEmail: String,
    patientAge: String,
    patientGender: String,
    patientPhone: String,
    question1: String,
    response1: String,
    question2: String,
    response2: String,
    question3: String,
    response3: String,
    enthusiasm: String,
    depressionScore: String,
    optimisum: String
})

module.exports = mongoose.model("Patient", patientSchema);
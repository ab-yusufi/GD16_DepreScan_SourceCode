const mongoose = require("mongoose");
const {ObjectId} = mongoose.Schema

var quizSchema = new mongoose.Schema({
    q1: {
        type: Array,
        default: [],
        required: true
    },
    q2: {
        type: Array,
        default: [],
        required: true
    },
    q3: {
        type: Array,
        default: [],
        required: true
    },
    q4: {
        type: Array,
        default: [],
        required: true
    },
    q5: {
        type: Array,
        default: [],
        required: true
    },
    q6: {
        type: Array,
        default: [],
    },
    q7: {
        type: Array,
        default: [],
    },
    q8: {
        type: Array,
        default: [],
    },
    q9: {
        type: Array,
        default: [],
    },
    q10: {
        type: Array,
        default: [],
    },
    ans: {
        type: Array,
        default: [],
        required: true
    },
    uid: {
        type: ObjectId,
        ref: 'User',
        required: true
    },
    category: {
        type: ObjectId,
        ref: 'Category',
        required: true
    },
    attempts: {
        type: ObjectId,
        ref: 'Attempt'
    },
    marks: {
        type: Number,
        required: true
    }
}, { timestamps: true })

module.exports = mongoose.model("Quiz", quizSchema);
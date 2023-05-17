const mongoose = require("mongoose");
const {ObjectId} = mongoose.Schema;

const attemptSchema = mongoose.Schema({
    quiz: {
        type: ObjectId,
        ref: 'Quiz',
        required: true,
    },
    name: {
        type: String,
        trim: true,
        required: true
    },
    score: {
        type: Number,
        required: true,
    },
    outof: {
        type: Number,
        required: true
    },
    uid: {
        type: ObjectId,
        ref: "User"
    },
    ans: {
        type: Array,
        default: [],
        required: true
    }
})

module.exports = mongoose.model("Attempt", attemptSchema);

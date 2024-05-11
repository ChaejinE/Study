const mongoose = require("mongoose");
const { Schema } = mongoose;
const { Types: { objectId }} = Schema;

const commentSchema = new Schema({
    commenter: {
        type: objectId,
        required: true,
        ref: "User" // Support to Populate by mongoose
    },
    comment: {
        type: String,
        required: true,
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model("Comment", commentSchema);

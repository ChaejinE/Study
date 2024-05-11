const express = require("express");
const User = require("../schemas/users");
const Comment = require("../schemas/comments");

const router = express.Router();

router.route('/')
    .get(async (req, res, next) => {
        try {
            const users = await User.find({});
            res.json(users);
        } catch (error) {
            console.error(error);
            next(error);
        }
    })
    .post(async (req, res ,next) => {
        try {
            const user = await User.create({
                name: req.body.name,
                age: req.body.age,
                married: req.body.married
            });
            console.log(user);
            res.status(201).json(user);
        } catch (error) {
            console.error(error);
            next(err);
        }
    });

router.get("/:id/comments", async(req, res, next) => {
    try {
        const comments = await Comment.find( {commenter: req.params.id}).populate();
        console.log(comments);
        res.json(commnets);
    } catch (error) {
        console.log(error);
        next(error);
    }
});

module.exports = router;

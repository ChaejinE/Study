const Post = require("../models/post");
const Hashtag = require("../models/hashtag");

exports.afterUploadImage = (req, res) => {
    res.json({url: `/img/${req.file.filename}`});
}

exports.uploadPost = async (req, res, next) => {
    try {
        const post = await Post.create({
            content: req.body.content,
            img: req.body.url,
            UserId: req.user.id,
        });
        const hashtags = req.body.content.match(/#[^\s#]*/g);
        if (hashtags) {
            Hashtag.findOrCreate({});
        }
    } catch (err) { 
        console.error(error);
        next(error);
    }
}

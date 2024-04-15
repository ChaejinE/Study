const User = require("../models/user");

exports.follow = async (req, res, next) => {
    try {
        const user = await User.findOne({ where: { id: req.user.id }});
        console.log("===============User : ", user);
        if (user) {
            await user.addFollowings(parseInt(req.params.id, 10));
            res.send("success");
        } else {
            res.status(404).send("no user");
        }
    } catch (error) {
        console.error(error);
        next(error);
    }
}

const User = require("../models/user")
const bcrypt = require("bcrypt"); 

exports.join = async (req, res, next) => {
    const { nick, email, password } = req.body;
    try {
        const exUser = await User.findOne({ where: { email }});
        if (exUser) {
            return res.redirect("/join?error=exist");
        }
        const hash = await bcrypt.hash(password, 12); // more longer more slower
        await User.create({
            email, nick, password: hash,
        });
        return res.redirect("/");
    } catch (err) {
        console.error(err);
        next(err);
    }
}

exports.login = () => {};
exports.logout = () => {};

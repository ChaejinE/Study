const User = require("../models/user");
const bcrypt = require("bcrypt");
const passport = require("passport");

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

exports.login = (req, res, next) => {
    // Middleware expansion pattern for using arguments like req, res, next
    passport.authenticate("local", (authError, user, info) => { // The arguments are passed by Strategy
        // failServer
        if (authError) {
            console.error(authError);
            return next(authError);
        }
        
        // failLogic
        if (!user) {
            return res.redirect(`/?loginError=${info.message}`);
        }
        
        // successLogin
        return req.login(user, (loginError) => {
            if (loginError) {
                console.error(loginError);
                return next(loginError);
            }
            return res.redirect("/");
        });
    })(req, res, next);
};

exports.logout = (req, res, next) => { 
    req.logout(() => { // remove session cookie from session object
        res.redirect("/");
    });
};

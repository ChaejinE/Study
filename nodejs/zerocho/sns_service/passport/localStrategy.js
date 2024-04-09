const passport = require("passport");
const bcrypt = require("bcrypt")
const { Strategy: LocalStrategy } = require("passport-local");
const User = require("../models/user");

module.exports = () => {
    passport.use(new LocalStrategy({
        usernameField: "email", // req.body.email
        passwordField: "password", // req.body.password
        passReqToCallback: false, // if true, you can use asnyc (req, email, password, done)
    }, async (email, password, done) => { // done(failServer, successUser, failLogic)
        try {
            const exUser = await User.findOne({ where: { email }});
            if (exUser) {
                const result = await bcrypt.compare(password, exUser.password);
                if (result) {
                    done(null, exUser)
                } else {
                    done(null, false, { message: "Invalid Password"});
                }
            } else {
                done(null, false, { message: "Not exist User" });
            }
        } catch (err) {
            console.error(err);
            done(err);
        }
    }));
};

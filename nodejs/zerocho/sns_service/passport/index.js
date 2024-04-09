const passport = require("passport");
const local = require("./localStrategy");
const kakao= require("./kakaoStrategy");
const User = require("../models/user");

module.exports = () => {
    passport.serializeUser((user ,done) => { // user === exUser
        done(null, user.id); // session { sessionCookie : userID } => for optimzation memory
        // But there is some issue for sharing session information
    });

    passport.deserializeUser((id, done) => { // Search info from { sessionCookie : userId } id === userId
        User.findOne({where: {id}}) // recovery to User Object => req.user
            .then((user) => done(null, user)) // user === User, at the sametime, req.session is maded
            .catch(err => done(err)); 
    })

    local();
    kakao();
}

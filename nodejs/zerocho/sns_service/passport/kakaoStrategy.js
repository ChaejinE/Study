const passport = require("passport");
const { Strategy: kakaoStrategy } = require("passport-kakao");
const User = require("../models/user")

module.exports = () => {
    passport.use(new kakaoStrategy({
        clientID: process.env.KAKAO_ID,
        callbackURL: "/uath/kakao/callback",
    }, async(accessToekn, refreshToken, profile, done) => {
        console.log("profile", profile); // It is always changed
        try {
            const exUser = await User.findOne({
                where: { snsId: profile.id, provider: "kakao" }
            });

            if (exUser) {
                // login
                done(null, exUser);
            } else {
                // signup
                const newUser = await User.create({
                    email: profile._json?.kakao_account?.email,
                    nick: profile.displayName,
                    snsId: profile.id,
                    provider: "kakao",
                })
                done(null, newUser);
            }

        } catch (err) {
            console.error(err);
            done()
        }
    }));
};

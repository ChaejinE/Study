const express = require("express");
const passport = require("passport");
const { isLoggedIn, isNotLoggedIn } = require("../middlewares");
const { join, login, logout } = require("../controllers/auth");
const router = express.Router();

router.post("/join", isNotLoggedIn, join);
router.post("/login", isNotLoggedIn, login);
router.get("/logout", isLoggedIn, logout);

router.get("/kakao", passport.authenticate("kakao")); // redirect kakao login window
router.get("/kakao/callback", passport.authenticate("kakao", { // if logged in, redirect this
    failureRedirect: "/?loginError=Fail to login Kakao"
}), (req, res) => {
    res.redirect('/');
})

module.exports = router;

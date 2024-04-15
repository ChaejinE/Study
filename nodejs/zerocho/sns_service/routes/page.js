const express = require("express");
const router = express.Router();
const { renderJoin, renderMain, renderProfile } = require("../controllers/page");
const { isLoggedIn, isNotLoggedIn } = require("../middlewares");

router.use((req, res, next) => {
    // res.locals : Shared data between middlewares
    res.locals.user = req.user; // If you are logged in, req.user is exist, else null
    res.locals.followerCount = req.user?.Followers?.length || 0;
    res.locals.followingCount = req.user?.Followings?.length || 0;
    res.locals.followingIdList = req.user?.Followings?.map(f => f.id) || [];

    // req.session.data : Shared data between users
    next();
});

router.get("/profile", isLoggedIn, renderProfile);
router.get("/join", isNotLoggedIn, renderJoin);
router.get("/", renderMain);

module.exports = router;

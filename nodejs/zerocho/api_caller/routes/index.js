const express = require("express");
const { getMyPosts, searchByHashtag, renderMain } = require("../controllers");
const router = express.Router();

router.get("/", renderMain);
router.get("/myposts", getMyPosts);
router.get("/search/:hashtag", searchByHashtag);

module.exports = router;

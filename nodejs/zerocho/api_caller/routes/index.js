const express = require("express");
const { test } = require("../controllers");
const { getMyPosts, searchByHashtag } = require("../controllers");
const router = express.Router();

router.get("/", async (req, res, next) => { 
    res.send("Main Test Page")}
);
router.get("/myposts", getMyPosts);
router.get("/search/:hashtag", searchByHashtag);

module.exports = router;

const express = require("express");
const { test } = require("../controllers");
const router = express.Router();

router.get("/", async (req, res, next) => { 
    res.send("Main Test Page")}
);
router.get("/test", test);

module.exports = router;

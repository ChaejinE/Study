const express = require("express");
const { verifyToken, apiLimiter, corsWhenDomainMatches } = require("../middlewares");
const { createToken, tokenTest, getMyPosts, getPostsByHashtag } = require("../controllers/v2");

const router = express.Router();

// 아래 로직으로 모든 CORS 상황을 대처할 수 없다.
// router.use((req, res, next) => {
//     res.setHeader("Access-Control-Allow-Origin", "http://localhost:4000");
//     res.setHeader("Access-Control-Allow-Headers", "content-type");
//     next();
// })

// router.use(cors({
//     origin: "http://localhost:4000",
//     // origin: true, // if credentials is true, it cant use '*'
//     credentials: true, // cookie request까지 필요하면 true로 set 해야됨
// }))

router.use(corsWhenDomainMatches);

router.post("/token", apiLimiter, createToken);
router.get("/test", verifyToken, apiLimiter, tokenTest);
router.get("/posts/my", verifyToken, apiLimiter, getMyPosts);
router.get("/posts/hashtag/:title", verifyToken, apiLimiter, getPostsByHashtag);

module.exports = router;

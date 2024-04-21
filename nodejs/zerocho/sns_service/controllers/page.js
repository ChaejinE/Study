const Post = require("../models/post");
const User = require("../models/user");
const Hashtag = require("../models/hashtag");

exports.renderProfile = (req, res, next) => {
    res.render("profile", { title: "내 정보 - NodeBird" });
};

exports.renderJoin = (req, res, next) => {
    res.render("join", { title: "회원 가입 - NodeBird"});
}

exports.renderMain = async (req, res, next) => {
    try {
        const posts = await Post.findAll({
            include: {
                model: User,
                attributes: ["id", "nick"]
            },
            order: [["createdAt", "DESC"]]
        })

        res.render("main", {
            title: "NodeBird",
            twits: posts,
        });

    } catch (error) {
        console.error(error);
        next(error);
    }
}

// Trend Develop Workflow : Router -> Controller -> Service(Request or Response)

exports.renderHashtag = async (req, res, next) => {
    const query = req.query.hashtag;
    console.log("Query : ", query);
    if (!query) {
        return res.redirect("/"); // 없을 때 대처방법
    }
    
    try {
        // 해쉬태그 찾고 딸린 게시글들 찾아서 렌더링
        const hashtag = await Hashtag.findOne({ where: { title: query }});
        let posts = [];
        if (hashtag) {
            posts = await hashtag.getPosts({
                include: [{ model: User, attributes: ["id", "nick" ]}],
                order: [["createdAt", "DESC"]]
            });
            console.log("HASH TAG : ", posts);
        }
        res.render("main", {
            title: `${query} | NodeBird`,
            twits: posts,
        })
    } catch (error) {
        console.error(error);
        next(error);
    }
}

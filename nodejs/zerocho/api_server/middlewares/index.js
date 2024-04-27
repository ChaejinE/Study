// 여러 Router에서 공통으로 사용되는 것들이 이 middleware에 선언된다.

const jwt = require("jsonwebtoken");

exports.isLoggedIn = (req, res, next) => {
    if (req.isAuthenticated()) {
        next();
    } else {
        res.status(403).send("Login 필요");
    }
};

exports.isNotLoggedIn = (req, res, next) => {
    if (!req.isAuthenticated()) {
        next();
    } else {
        const message = encodeURIComponent("Login 상태입니다");
        res.redirect(`/?error=${message}`);
    }
}

exports.verifyToken = async (req, res, next) => {
    try {
        res.locals.decoded = jwt.verify(req.headers.authorization, process.env.JWT_SECRET);
        return next();
    } catch (err) {
        if (err.name == "TokenExpiredError") {
            res.status(419).json({
                code: 419,
                message: "Expired Token"
            })
        }

        return res.status(401).json({
            code: 401,
            message: "Invalid Token"
        })
    }
}

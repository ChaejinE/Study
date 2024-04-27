// 여러 Router에서 공통으로 사용되는 것들이 이 middleware에 선언된다.

const jwt = require("jsonwebtoken");
const rateLimit = require("express-rate-limit");
const cors = require("cors");
const { User, Domain } = require("../models");

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

exports.apiLimiter = async (req, res, next) => {
    // middleware expansion pattern for per type
    let user;
    if (res.locals.decoded) {
        user = User.findOne({ where: { id: res.locals.decoded.id }});
    }
    rateLimit({
        windowMs: 60 * 1000,
        max: user?.type === "preminum" ? 1000 : 10,
        hanlder(req, res) {
            res.status(this.statusCode).json({
                code: this.statusCode,
                message: "You can request only one at onece"
            })
        }
    })(req, res, next);
}

exports.deprecated = (req, res) => {
    res.status(410).json({
        code: 410,
        message: "Please Use New Veresion"
    })
}

exports.corsWhenDomainMatches = async (req, res, next) => {
    const domain = await Domain.findOne({
        where: {host: new URL(req.get("origin")).host}
    });
    
    if (domain) {
        cors({
            origin: req.get("origin"),
            credentials: true,
        })(req, res, next);
    } else {
        next();
    }
}

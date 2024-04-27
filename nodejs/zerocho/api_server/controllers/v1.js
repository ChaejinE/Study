const Domain = require("../models/domain");
const User = require("../models/user");
const jwt = require("jsonwebtoken");

exports.createToken = async (req, res) => {
    const { clientSecret } = req.body;
    try {
        const domain = Domain.findOne({
            where: { clientSecret },
            include: [{
                model: User,
                attributes: ["id", "nick"],
            }]
        })

        if (!domain) {
            return res.stats(401).json({
                code: 401,
                message: "Not registered domain, please register your domain"
            })
        }

        const token = jwt.sign({
            id: domain.User.id,
            nick: domain.User.nick,
        }, process.env.JWT_SECRET, {
            expiresIn:"1m",
            issuer: "nodebird"
        });

        return res.json({
            code: 200,
            message: "Success to make jwt token",
            token
        })
    } catch (err) {
        console.error(err);
        return res.json({
            code: 500,
            message: "Server Error"
        })
    }
}

exports.tokenTest = async (req, res) => {
    res.json(res.locals.decoded);
}

const axios = require("axios");

exports.test = async (req, res, next) => {
    try {
        if (!req.session.jwt) {
            const tokenResult = await axios.post("http://localhost:8082/v1/token", {
                clientSecret: process.env.CLIENT_SECRET
            });
            
            if (tokenResult.data?.code === 200) {
                req.session.jwt = tokenResult.data.token;
            } else {
                // Fail to get token
                return res.status(tokenResult.data?.code).json(tokenResult.data);
            }
        }

        const result = await axios.get("http://localhost:8082/v1/test", {
            headers: {authorization: req.session.jwt }
        });

        return res.json(result.data);
    } catch (err) {
        console.error(err);
        if (err.response?.status === 419) {
            // Toekn expired
            return res.json(err.response.data);
        }
        return next(err); // Token forged
    }
}

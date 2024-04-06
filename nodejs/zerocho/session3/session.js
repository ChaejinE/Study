const http = require("http");
const url = require("url");
const qs = require("querystring")
const fs = require("fs").promises

// Cookie는 외부인의 조작의 위험이 있음
const parseCookies = (cookie = ' ') => 
    cookie
        .split(";")
        .map(v => v.split('='))
        .reduce((acc, [k ,v]) => {
            acc[k.trim()] = decodeURIComponent(v);
            return acc;
        }, {})

const session = {};

http.createServer(async (req, res) => {
    const cookies = parseCookies(req.headers.cookie);

    if (req.url.startsWith("/login")) {
        const { query } = url.parse(req.url); // extract query string
        const { name } = qs.parse(query);
        const expires = new Date();
        expires.setMinutes(expires.getMinutes() + 5);
        const uniqueInt = Date.now();
        // session에 사용자를 식별한 정보를 담는다.
        session[uniqueInt] = {
            name, expires
        }
        
        // 외부 사용자가 알아볼 수 없는 내용 uniqueInt을 세션에 넣어서 전달한다.
        res.writeHead(302, {
            Location: "/",
            "Set-Cookie": `session=${uniqueInt}; name=${encodeURIComponent(name)}; Expires=${expires.toGMTString()}; HttpOnly; Path=/`
        })
        res.end();
    } else if (cookies.session && session[cookies.session]?.expires > new Date()) {
        res.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
        res.end(`${session[cookies.session].name}님 안녕하세요`);
    } else {
        try {
            const data = await fs.readFile("cookie.html");
            res.writeHead(200, {"Content-Type": "text/html; charset=utf-8"});
            res.end(data);
        } catch (err) {
            res.writeHead(500, {"Content-Type": "text/html; charset=utf-8"});
            res.end(err.message);
        }
    }

})
    .listen(8083, () => {
        console.log("8083 Port !!")
    })

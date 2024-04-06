const http = require("http");
const fs = require("fs").promises;

const server = http.createServer(async (req, res) => {
    try {
        res.writeHead(200, {"Content-Type": "text/html; charset=utf-8"});
        // res.write("<h1>Hello</h1>");
        // res.write("<h2>Hello</h2>");
        // res.end("<p>lotto</p>");
        const data = await fs.readFile("./server.html");
        res.end(data);
    } catch (err) {
        res.writeHead(200, {"Content-Type": "text/html; charset=utf-8"});
        console.error(err);
        res.end(err.message);
    }
})
    .listen(8080);

server.on("listening", () => {
    console.log("8080 port !!!!!")
})

server.on("error", (err) => {
    console.error(err);
})

const http = require("http");

const server = http.createServer((req, res) => {
    res.write("<h1>Hello</h1>");
    res.write("<h2>Hello</h2>");
    res.end("<p>lotto</p>");
})
    .listen(8080);

server.on("listening", () => {
    console.log("8080 port !!!!!")
})

server.on("error", (err) => {
    console.error(err);
})

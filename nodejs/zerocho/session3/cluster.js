const cluster = require("cluster");
const http = require("http");
const numCPUs = require("os").cpus().length;

if (cluster.isMaster) {
    console.log(`"Master Process ID : ${process.pid}`);
    console.log(`Worker nums : ${numCPUs}`);
    for (let i = 0; i < numCPUs; i += 1) {
        cluster.fork();
    }

    cluster.on("exit", (worker, code, signal) => {
        console.log(`${worker.process.pid} Worker가 종료되었습니다.`)
        console.log("code", code, "signal", signal);
        // Recovery ?
        // cluster.fork()
    });
} else {
    http.createServer((req, res) => {
        res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
        res.write("<h1> Hello Lotto </h1>");
        res.end("<p> Lotto Cluster ! </p>");
        setTimeout(() => {
            process.exit(1);
        }, 1000);
    })
        .listen(8086);
}

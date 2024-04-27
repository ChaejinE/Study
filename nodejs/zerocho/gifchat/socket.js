// const WebSocket = require('ws');
const SocketIO = require("socket.io");

module.exports = (server) => {
    // WebSocket은 Server와 Port를 공유한다.
    // Server는 HTTP Protocol인데 비해 WebSocket은 WS Protocol 이다.
    // const wss = new WebSocket.Server({ server });
    const io = SocketIO(server, { 
        path: "/socket.io" 
    }); // Add path for client

    io.on("connection",  (socket) => {
        const req = socket.request;
        const ip = req.headers["x-forwarded-for"] || req.socket.remoteAddress;
        console.log("New Client Access", ip, socket.id, req.ip);
        socket.on("disconnect", () => {
            console.log("Client Close", socket.id);
            clearInterval(socket.interval);
        })
        socket.on("reply", (data) => {
            console.log(data);
        })
        socket.on("error", console.error);
        socket.interval = setInterval(() => {
            socket.emit("new", "Hello Socket.IO"); 
        }, 3000);
    })

    // wss.on("connection",  (ws, req) => {
    //     const ip = req.headers["x-forwarded-for"] || req.socket.remoteAddress;
    //     console.log("New Client Access", ip);
    //     ws.on("message", (message) => {
    //         console.log(message.toString()); // message is a buffer
    //     })
    //     ws.on("error", console.error);
    //     ws.on("close", () => {
    //         console.log("Client Close", ip);
    //         clearInterval(ws.interval);
    //     })
    //     ws.interval = setInterval(() => {
    //         if (ws.readyState === ws.OPEN) {
    //             ws.send("Send text from Server to Client");
    //         }
    //     }, 3000);
    // })
}

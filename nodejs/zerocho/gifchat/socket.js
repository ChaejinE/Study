// const WebSocket = require('ws');
const SocketIO = require("socket.io");
const { removeRoom } = require("./services");

module.exports = (server, app, sessionMiddleware) => {
    // WebSocket은 Server와 Port를 공유한다.
    // Server는 HTTP Protocol인데 비해 WebSocket은 WS Protocol 이다.
    // const wss = new WebSocket.Server({ server });
    const io = SocketIO(server, { 
        path: "/socket.io" 
    }); // Add path for client
    app.set("io", io);

    const room = io.of("/room");
    const chat = io.of("/chat");
    // socket.io에서의 MiddleWare를 express MiddleWare처럼 사용하게 하기
    const wrap = middleware => (socket, next) => middleware(socket.request, {}, next);
    chat.use(wrap(sessionMiddleware));

    room.on("connection", (socket) => {
        console.log("Access Room Namespace");
        socket.on("disconnect", () => {
            console.log("Disconnect Room Namespace");
        })
    });

    chat.on("connection", (socket) => {
        console.log("Access Chat  Namespace");
        socket.on("join", (data) => {
            socket.join(data);
            socket.to(data).emit("join", {
                user: "system",
                chat: `${socket.request.session.color}님이 입장하셨습니다.`
            });
        });

        socket.on("disconnect", async () => {
            console.log("Disconnect Chat Namespace");
            const { referer } = socket.request.headers;
            const roomId = new URL(referer).pathname.split('/').at(-1);
            const currentRoom = chat.adapter.rooms.get(roomId);
            const userCount = currentRoom?.size || 0;
            if (userCount === 0 ) {
                await removeRoom(roomId);
                room.emit("removeRoom", roomId);
                console.log("Success to remove the room");
            } else {
                socket.to(roomId).emit("exit", {
                    user: "system",
                    chat: `${socket.request.session.color}님이 나가셨습니다.`
                });
            }
        });
    });

    // io.on("connection",  (socket) => {
    //     const req = socket.request;
    //     const ip = req.headers["x-forwarded-for"] || req.socket.remoteAddress;
    //     console.log("New Client Access", ip, socket.id, req.ip);
    //     socket.on("disconnect", () => {
    //         console.log("Client Close", socket.id);
    //         clearInterval(socket.interval);
    //     })
    //     socket.on("reply", (data) => {
    //         console.log(data);
    //     })
    //     socket.on("error", console.error);
    //     socket.interval = setInterval(() => {
    //         socket.emit("new", "Hello Socket.IO"); 
    //     }, 3000);
    // })

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

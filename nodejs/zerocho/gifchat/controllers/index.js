const Room = require("../schemas/room");
const Chat = require("../schemas/chat");
const { removeRoom: _removeRoomService } = require("../services");

exports.renderMain = async (req, res, next) => {
    try {
        const rooms = await Room.find({});
        res.render("main", { rooms, title: "GIF Chat Room" });
    } catch (error) {
        console.error(error);
        next(error);
    }
};
exports.renderRoom = (req, res, next) => {
    res.render("room", { title: "GIF Chat Room" });
};
exports.createRoom = async  (req, res, next) => {
    try {
        const newRoom = await Room.create( {
            title: req.body.title,
            max: req.body.max,
            owner: req.session.color,
            password: req.body.password
        })

        const io = req.app.get('io');
        io.of("/room").emit("newRoom", newRoom);
        if (req.body.password) {
            res.redirect(`/room/${newRoom._id}?=password=${req.body.password}`);
        } else {
            res.redirect(`/room/${newRoom._id}`);
        }
    } catch (error) {
        console.error(error);
        next(error);
    }
};

exports.enterRoom = async (req, res, next) => {
    try {
        const room = await Room.findOne({_id: req.params.id });
        if (!room) {
            return res.redirect("/?error=Not Exist Room");
        }
        if (room.password && room?.password !== req.query.password) {
            return res.redirect("/?error=Invalid Password");
        }

        const io = req.app.get("io");
        const { rooms } = io.of("chat").adapter;
        if (rooms.max <= rooms.get(req.params.id)?.size) {
            return res.redirect("/?error=Exceed Max Users")
        }
        const chats = await Chat.find({room: room._id}).sort("createdAt");
        res.render("chat", { title: "Create GIF Chat Room", chats, room, user: req.session.color });
    } catch (error) {
        console.error(error);
        next(error); 
    }
};

exports.removeRoom = async (req, res, next) => {
    try {
        await _removeRoomService(req.params.id);
        res.send("ok");
    } catch (error) {
        console.error(error);
        next(error);
    }
}; 

exports.sendChat = async (req, res, next) => {
    try {
        const chat = await Chat.create({
            room: req.params.id,
            user: req.session.color,
            chat: req.body.chat
        });
        req.app.get("io").of("/chat").to(req.params.id).emit("chat", chat);
        res.send("ok");
    } catch (error) {
        console.error(error);
        next(error);
    }
}

exports.sendGif = async (req, res, next) => {
    try {
        const chat = await Chat.create({
            room: req.params.id,
            user: req.session.color,
            gif: req.file.filename
        })
        req.app.get("io").of("/chat").to(req.params.id).emit("chat", chat);
        res.send("ok");
    } catch (error) {
        console.error(error);
        next(error);
    }
}

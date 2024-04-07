const dotenv = require("dotenv");
const express = require("express");
const morgan = require("morgan");
const cookieParser = require("cookie-parser");
const session = require("express-session");
const multer = require("multer");
const fs = require("fs");
const path = require("path");
const app = express();

dotenv.config();
app.set("uploadDirName", "uploads")
try {
    fs.readdirSync(app.get("uploadDirName"));
} catch (err) {
    console.log(`${err}\nSo Create directory`);
    fs.mkdirSync(app.get("uploadDirName"));
}

const upload = multer({
    storage: multer.diskStorage({
        destination(req, file, done) {
            // The second argument is operated when it is success
            done(null, app.get("uploadDirName"));
        },
        filename(req, file, done) {
            const ext = path.extname(file.originalname);
            done(null, path.basename(file.originalname, ext) + Date.now() + ext);
        },
    }),
    limits: {fileSize: 5 * 1024 * 1024},
})

// method(HTTP) + path = Router
// Middelwares
app.set("port", process.env.PORT || 8081);

app.use(morgan("combined")); // GET, HOSTNAME 등을 console
// Static Middleware
// req 경로와 real 경로를 다르게 보이게 할 수 있음. 보통 맨위에 위치해야함
app.use(cookieParser(process.env.COOKIE_SECRET)); // cookie를 자동으로 parsing req.cookies
app.use(session({
    resave: false,
    saveUninitialized: false,
    secret: process.env.COOKIE_SECRET,
    cookie: {
        httpOnly: true,
    },
    name: "lotto.sid"
}))
app.use("/", (req, res, next) => {
    // middleware expansion
    if (req.session.id) {
        express.static(__dirname)(req, res, next);
    } else {
        next();
    }
});
app.use(express.json()); // json data json으로
app.use(express.urlencoded({ extended: true })); // form data 처리
app.use((req, res, next) => {
    console.log("[Common] There is some requets !")
    req.session.data = "hello-lotto" // User에 한해서 유지하려할때
    req.data = "hi-middleware" // 다른 미들웨어로 데이터를 보내고 싶을 때
    next();
}, (req, res, next) => {
    // If error argument pass to next, it will go to error handler
    try {
        console.log("Next 1 Middle Ware");
        next();
    } catch (err) {
        next(err);
    }
}, (req, res, next) => {
    try {
        console.log("Next 2 Middle Ware");
        next();
    } catch (err) {
        next(err);
    }
})
app.use("/about", (req, res, next) => {
    console.log("[About Common] I love about !")
    next()
})

// Routers
app.get("/", (req, res) => {
    const index_path = path.join(__dirname, "index.html");
    console.log(`Send : ${index_path}`)
    console.log(req.data);
    console.log(req.session.data);
    // console.log(req.cookies);
    res.sendFile(index_path);
})

// single
app.post('/upload', upload.single("image"), (req, res) => {
    console.log(req.file);
    res.send("OK")
})

// multi using multi-part
app.post('/upload', upload.array("image"), (req, res) => {
    console.log(req.files);
    res.send("OK")
})

// multi using multi-part without file
app.post('/upload', upload.none(), (req, res) => {
    console.log(req.body.title)
    res.send("OK")
})

// multi using multi form-data
app.post('/upload', upload.fields({name : "image1"}, {name: "image2"}), (req, res) => {
    console.log(req.files.image1);
    console.log(req.files.image2);
    res.send("OK")
})

app.get("/about", (req, res) => {
    const about_path = path.join(__dirname, "about.html");
    console.log(`Send : $${about_path}`);
    res.sendFile(about_path);
})

app.get("/error", () => {
    throw new Error("Erorr intended")
})

// :name is wild card
app.get("/about/:name", (req, res) => {
    console.log(`Name : ${req.params.name}`);
})
app.listen(app.get("port"), () => {
    console.log("Express Start !");
})

// Error Middlewares
app.use((req, res, next) => {
    res.status(200).send("404 NotFound -- lotto --");
})
// The arguments of the error middleware should be 4
// The reason that write 200 status is for the security
app.use((err, req, res, next) => {
    console.error("Error Log !");
    res.status(200).sendFile(path.join(__dirname, "error.html"))
})

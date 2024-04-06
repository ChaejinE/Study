const express = require("express");
const morgan = require("morgan");
const cookieParser = require("cookie-parser");
const session = require("express-session");
// const multer = require("multer");
const path = require("path");
const app = express();

// method(HTTP) + path = Router
// Middelwares
app.set("port", process.env.PORT || 8081);

app.use(morgan("combined")); // GET, HOSTNAME 등을 console
app.use("/", express.static(__dirname)); // req 경로와 real 경로를 다르게 보이게 할 수 있음. 보통 맨위에 위치해야함
app.use(cookieParser("signed")); // cookie를 자동으로 parsing req.cookies
app.use(express.json()); // json data json으로
app.use(express.urlencoded({ extended: true })); // form data 처리
app.use((req, res, next) => {
    console.log("[Common] There is some requets !")
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
    console.log(req.cookies);
    const name="test"
    res.cookie("name", encodeURIComponent(name), {
        expires: new Date(),
        httpOnly: true,
        path: "/'"
    })
    res.sendFile(index_path);
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

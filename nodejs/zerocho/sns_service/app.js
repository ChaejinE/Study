const express = require("express");
const cookieParser = require("cookie-parser");
const morgan = require("morgan");
const path = require("path");
const session = require("express-session");
const nunjucks = require("nunjucks");
const dotenv = require("dotenv");
const passport = require('passport')
const { sequelize } = require("./models");

dotenv.config();
const pageRouter = require("./routes/page");
const authRouter = require("./routes/auth");
const postRouter = require("./routes/post");
const passportConfig = require("./passport");
const userRouter = require("./routes/user");


const app = express();
passportConfig();
app.set("port", process.env.PORT || 8001);
app.set("view engine", "html");
nunjucks.configure("views", {
    express: app,
    watch: true,
})

sequelize.sync({ force: false })
    .then(() => {
        console.log("Success to connect DB");
    })
    .catch((err) => {
        console.error(err);
    })

app.use(morgan("dev"));
app.use(express.static(path.join(__dirname, "public")));
app.use("/img", express.static(path.join(__dirname, "uploads")));
app.use(express.json()); // req.body crated ! from ajax json request
app.use(express.urlencoded({ extended: false })); // req.body created ! from form-data
app.use(cookieParser(process.env.COOKIE_SECRET));
app.use(session( {
    resave: false,
    saveUninitialized: false,
    secret: process.env.COOKIE_SECRET,
    cookie: {
        httpOnly: true,
        secure: false, // when it use https
    }
}))
// middlewares of passort should be on the next of session
app.use(passport.initialize()); // req.user, req.login, req.isAuthenticated, req.logout created !
app.use(passport.session()) // connect.sid -> session cookie -> Browser;

app.use("/", pageRouter);
app.use("/auth", authRouter);
app.use("/post", postRouter);
app.use("/user", userRouter);
app.use((req, res, next) => {
    const error = new Error(`${req.method} ${req.url} there is no router`);
    error.status = 404;
    next(error);
});
app.use((err, req, res, next) => {
    res.locals.message = err.message;
    res.locals.error = process.env.NODE_ENV !== "production" ? err: {};
    res.status(err.status || 500);
    res.render("error"); // it is sended by nunjucks
});

app.listen(app.get("port"));

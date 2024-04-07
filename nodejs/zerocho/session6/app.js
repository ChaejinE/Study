const express = require("express");
const path = require("path");
const morgan = require("morgan");
const nunjucks = require("nunjucks");

const { sequelize } = require("./models");
const indexRouter = require("./routes");
const userRouter = require("./routes/users");
const commentRouter = require("./routes/comments");

app = express();
app.set("port", process.env.PORT || 8083);
app.listen(app.get("port"), () => {
    console.log("Server Start : ", app.get("port"))
});
app.set("view engine", "html");
nunjucks.configure("views", {
    express: app,
    watch: true,
});

app.use(morgan("dev"));
app.use(express.static(path.join(__dirname, "public")));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use("/", indexRouter);
app.use("/users", userRouter);
app.use("/comments", commentRouter);

sequelize.sync({force: false})
    .then(() => {
        console.log("Success to connect the DB");
    })
    .catch((err) => {
        console.error(err);
    })

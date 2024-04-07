const express = require("express");
const indexRouter = require("./routes");
const userRouter = require("./routes/user");
// const path = require("path");

const app = express();
app.listen(process.env.PORT | 8083);
// template engine - pug setting
// app.set("views", path.join(__dirname, "views"));
// app.set("veiw engine", "pug");
app.use("/", indexRouter);
app.use("/user", userRouter);

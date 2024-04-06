const express = require("express");
const path = require("path");
const app = express();

app.set("port", process.env.PORT || 8081);

app.get("/", (req, res) => {
    const index_path = path.join(__dirname, "index.html");
    console.log(`Send : ${index_path}`)
    res.sendFile(index_path);
})

app.listen(app.get("port"), () => {
    console.log("Express Start !")
})

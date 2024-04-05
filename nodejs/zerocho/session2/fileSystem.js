const fs = require("fs").promises;

fs.readFile("./readme.txt")
    .then((data) => {
    console.log(data);
    console.log(data.toString());
    })
    .catch((err) => {
        throw err;
    })

fs.writeFile("./writeme.txt", "Oh my text")
    .then(() => {
        return fs.readFile("./writeme.txt")
    })
    .then((data) => {
        console.log(data.toString())
    })

const mongoose = require("mongoose");

const connect = () => {
    if (process.env.NODE_ENV != "production") {
        mongoose.set("debug", true); // For checking queries
    }
    
    uri = "mongodb://root:qwerqwer123@localhost:27017/admin"
    mongoose.connect(uri, { 
        dbName: "nodejs", 
        useNewUrlParser: true,
    }, (error) => {
        if (error) {
            console.error("MongoDB Connection Error", error);
        } else {
            console.log("MongoDB Connection Success");
        }
    })
}

mongoose.connection.on("error", (error) => {
    console.error("MongoDB Connection Error", error);
});

mongoose.connection.on("disconnected", () => {
    console.log("MongoDB Disconnected, Try to reconnect");
    connect();
});

module.exports = connect;

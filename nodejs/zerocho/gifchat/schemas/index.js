 const mongoose = require("mongoose");

 const connect = () => {
    if (process.env.NODE_ENV !== "production") {
        mongoose.set("debug", true);
    }

    mongoose.connect(`mongodb://${process.env.MONGO_ID}:${process.env.MONGO_PASSWORD}@localhost:27017/admin`, {
        dbName: "nodejs",
        useNewUrlParser: true,
    }).then(() => {
        console.log("MongoDB Connection Succes");
    }).catch(error => {
        console.error(`MongoDB Connection Error:\n${error}`);
    })
 }

mongoose.connection.on("error", (error) => {
    console.error(`MongoDB Connection Error:\n${error}`);
})

mongoose.connection.on("disconnected", (error) => {
    console.error(`MongoDB Connection Disconnect So Try to Retry !`);
    connect();
})

module.exports = connect;

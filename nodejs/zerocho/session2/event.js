const EventEmitter = require("events");

const myEvent = new EventEmitter();

myEvent.addListener("event1", () => {
    console.log("Event 1")
})

myEvent.on("event2", () => {
    console.log("Event 2")
})

myEvent.emit("event2");
myEvent.emit("event1");

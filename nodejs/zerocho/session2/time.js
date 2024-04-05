console.time("Time")
const immediate = setImmediate(() => {
    console.log("Background");
})
console.log("hi")
console.timeEnd("Time")

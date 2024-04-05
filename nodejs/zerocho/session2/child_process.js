const exec = require("child_process").exec;

var process = exec("echo hi");

process.stdout.on("data", function(data) {
    console.log(data.toString());
})

process.stderr.on("data", function(data) {
    console.error(data.toString());
})

const spawn = require("child_process").spawn;
const process2 = spawn("python3", ["hello.py"])

process2.stdout.on("data", function(data) {
    console.log(data.toString());
})

process2.stderr.on("data", function(data) {
    console.error(data.toString());
})

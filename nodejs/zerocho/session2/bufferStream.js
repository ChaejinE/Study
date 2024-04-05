const buffer = Buffer.from("버퍼로 바꿔줘")
console.log(buffer);
console.log(buffer.length);
console.log(buffer.toString());

const array = [Buffer.from("안녕"), Buffer.from("하세요"), Buffer.from("!!!!")];
console.log(Buffer.concat(array).toString());

console.log(Buffer.alloc(5));

const fs = require("fs");
const readStream = fs.createReadStream("./buffer.txt", {highWaterMark: 16}); // 64KB at once

const data = [];
readStream.on("data", (chunk) => {
    data.push(chunk);
    console.log("data: ", chunk, chunk.length);
})
readStream.on("end", () => {
    console.log("end: ", Buffer.concat(data).toString());
})
readStream.on("error", (err) => {
    console.error(err);
})

// 메모리를 아낀다

const fs2 = require("fs");
const writeStream = fs.createWriteStream("./writeStream.txt");

writeStream.on("finish", () => {
    console.log("Success to write");
})

writeStream.write("이 글을 씁니다.\n");
writeStream.write("한번 더 씁니다.");
writeStream.end();

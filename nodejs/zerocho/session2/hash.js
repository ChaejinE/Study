const crypto = require("crypto")

console.log("base64: ", crypto.createHash("sha512").update("pwd").digest("base64"))
console.log("base64: ", crypto.createHash("sha512").update("pwd").digest("hex"))

// 보통 암호 Hash 시, bcrypt 사용. Node에서는 pdkdf2 scrypt만 지원

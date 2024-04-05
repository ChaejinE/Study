const crypto = require("crypto")

const pass = 'pass';
const salt = 'salt';
const start = Date.now();

// node는 background에서 thread가 4개씩 기본적으로 동시에 돌아간다.

const os = require("os")
const core_nums = os.cpus().length
console.log("Core : ", core_nums)
// 코어 최대 개수로 최적화 가능하다.
process.env.UV_THREADPOOL_SIZE = core_nums

crypto.pbkdf2(pass, salt, 1_000_000, 128, "sha512", () => {
    console.log("1", Date.now() - start);
})

crypto.pbkdf2(pass, salt, 1_000_000, 128, "sha512", () => {
    console.log("1", Date.now() - start);
})

crypto.pbkdf2(pass, salt, 1_000_000, 128, "sha512", () => {
    console.log("1", Date.now() - start);
})

crypto.pbkdf2(pass, salt, 1_000_000, 128, "sha512", () => {
    console.log("1", Date.now() - start);
})

crypto.pbkdf2(pass, salt, 1_000_000, 128, "sha512", () => {
    console.log("1", Date.now() - start);
})

crypto.pbkdf2(pass, salt, 1_000_000, 128, "sha512", () => {
    console.log("1", Date.now() - start);
})

crypto.pbkdf2(pass, salt, 1_000_000, 128, "sha512", () => {
    console.log("1", Date.now() - start);
})

crypto.pbkdf2(pass, salt, 1_000_000, 128, "sha512", () => {
    console.log("1", Date.now() - start);
})

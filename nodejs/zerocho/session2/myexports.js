console.log(this === globalThis) // module.exports

function test(){
    console.log(this === globalThis)
}

test()

const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const MongoClient = require('mongodb').MongoClient;
app.set('view engine', 'ejs')

var db;
MongoClient.connect("mongodb+srv://cjlotto:1234@cluster0.x4bssi5.mongodb.net/?retryWrites=true&w=majority",
    (err, client) => {
        if (err) return console.log(err);

        db = client.db("TODOApp");
        app.listen(8080, function () { console.log('listening on 8080') });
    })

app.use(bodyParser.urlencoded({ extended: true }));
app.get('/', function (request, response) { response.sendFile(__dirname + "/index.html") });
app.get('/write', (request, response) => { response.sendFile(__dirname + "/write.html"); console.log("전송 성공"); });
app.get('/list', (request, response) => {
    db.collection('post').find().toArray((err, result) => {
        response.render('list.ejs', { posts: result });
    })
});

app.post('/add', (request, response) => {
    response.send("add 실행");
    db.collection('counter').findOne({ name: '게시물 개수' }, (err, result) => {
        console.log(result.totalPost)
        var totalPost = result.totalPost;
        var data = { _id: totalPost + 1, 제목: request.body.title, 날짜: request.body.date };
        db.collection('post').insertOne(data, (err, result) => {
            if (err) return response.send("Fail to post");
            db.collection('counter').updateOne({ name: '게시물 개수' }, { $inc: { totalPost: 1 } }, (err, result) => {
                if (err) return response.send("Fail to update");
            });
        });
    });
});

app.delete('/delete', (req, resp) => {
    console.log(req.body);
    req.body._id = parseInt(req.body._id); // {_id : '1'} 이런식으로 value가 string으로 수신됨.
    db.collection('post').deleteOne(req.body, (err, result) => {
        if (err) { resp.status(400).send({ message: "Fail" }); } // Client의 실수 에러 코드
        resp.status(200).send({ message: "Success" });
    });
});
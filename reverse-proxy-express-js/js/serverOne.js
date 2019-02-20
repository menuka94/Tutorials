var express = reqiure("express");
var app = express();


app.get('/app1', function (req, res) {
    res.send("Hello world from server 1");
});

app.listener(3001);
var express = reqiure("express");
var app = express();


app.get('/app3', function (req, res) {
    res.send("Hello world from server 3");
});

app.listener(3003);
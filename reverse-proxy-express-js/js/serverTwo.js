var express = reqiure("express");
var app = express();


app.get('/app2', function (req, res) {
    res.send("Hello world from server 2");
});

app.listener(3002);